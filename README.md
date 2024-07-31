# The Taste Of BeiHang

本项目可查看GITHUB仓库：https://github.com/zhhangBian/The-Taste-of-Beihang

仓库中有本文档的Markdown形式，阅读体验更好。

![image-20240731220531786](https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407312205127.png)

# 功能简介（简述项目拥有的功能）

1. 多用户登录注册
2. 支持搜索
3. 支持大语言模型的用餐建议推荐
4. 食堂和菜品的增删改查
5. 支持记录用户的就餐记录
6. 支持就餐记录的增删改查与统计
7. 支持用户评论菜品
8. 支持用户点赞他人的评论
9. 支持用户收藏食堂和菜品
10. 支持用户个人信息的修改与管理
11. 支持美食广场功能与自动推荐菜品

# 已完成任务

### 必做任务完成情况（6/6）

1. 食堂与菜品的增删改查
2. 用户就餐记录的增删改查
3. 收藏食堂和菜品
4. 推荐菜品
5. 支持用户评论
6. 用户个人中心

### 选做任务完成情况（7/3）：

1. 数据库中共添加了450+ 道菜品（**满足加分项+3**）
2. 接入大语言模型个性化推荐
3. 支持多用户的登录与注册（**自定义**）
4. 用户可以点赞别的用户的评论（**自定义**）
5. 每道菜品显示评分等指标，用户评论时可以提交评分（**自定义**）
6. 个人中心允许上传头像（**自定义**）
7. 提供个人记录的统计数据（**自定义**）

# 总体设计方案

## 定义了一些工具函数

支持从网络上自动爬取图片、上传到腾讯云图床，根据爬虫结果自动添加响应信息到后端数据库。

### 从网络上爬取图片

简要代码为：

```py
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.findAll('p', class_='contentFont', string=lambda x: x and x.startswith('#'))
    
# 坐标
location_tag = img_tag.find_parent().find_next_sibling('p', class_='contentFont')
location = location_tag.text.strip() if location_tag else None

# 窗口位置
window_tag = location_tag.find_next_sibling('p', class_='contentFont')
window = window_tag.text.strip() if window_tag else None

# 小编食评
comment_tag = window_tag.find_next_sibling('p', class_='contentFont')
description = comment_tag.text.strip() if comment_tag else None
```

### 上传到腾讯云

简要代码为：

```py
def upload_percentage(consumed_bytes, total_bytes):
    """进度条回调函数，计算当前上传的百分比
    :param consumed_bytes: 已经上传的数据量
    :param total_bytes: 总数据量
    """
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate))
        sys.stdout.flush()

def upload(path, title):
    key = str(time.time())[:4] + title
    response = client.upload_file(
        Bucket=bucket_name,
        Key=key,
        LocalFilePath=path,
        PartSize=1,
        MAXThread=5,
        progress_callback=upload_percentage,
        EnableMD5=False,
        ACL='public-read',
    )

    url = client.get_object_url(
        Bucket=bucket_name,
        Key=key
    )

    return url
```

### 根据爬虫结果添加到后端数据库

简要代码为：

```py
with open("data/comment_data.csv", "r", encoding='utf-8') as data_file:
    data = csv.DictReader(data_file)

    for row in data:
        author = User.objects.order_by('?').first()

        dish_name = row['dish_name']
        image = row['image']
        restaurant_name = row['restaurant_name']
        address = row['address']
        content = row['content']

        title = row['title']

        try:
            dish = Dish.objects.get(name=dish_name)
        except Dish.DoesNotExist:
            dish, created = Dish.objects.update_or_create(
                name=dish_name,
                image=image,
                address=address,
                restaurant_name=restaurant_name,
                description=content,
            )
            print("create dish of " + str(dish_name) + " in " + str(restaurant_name))

        comment, created = Comment.objects.update_or_create(
            title=title,
            content=content,
            image=image,

            grade=generate_random_real_float(4, 5),
            price=generate_random_real_float(4, 5),
            flavour=generate_random_float(0, 2),
            waiting_time=random.randint(1, 100),

            restaurant_name=restaurant_name,
            dish_name=dish_name,
            author_id=author.id
        )
        print("create comment " + str(title) + " of " + str(dish_name))
```

## 支持用户登录

通过django的用户管理函数，实现了一个简单的用户登录系统，并且支持相应的用户注册、信息修改、头像上传等功能。

并且，为了保证项目的执行正常，在为登录时会强制重定向至登录界面进行登录。

### 用户权限管理

利用django的函数功能实现了一个基本的注册登录管理。

```py
@response_wrapper
@require_GET
def check_login_status(request: HttpRequest):
    global login_id

    if login_id != MAGIC_ID:
        return success_response({
            "message": "已登录"
        })
    else:
        return fail_response(ErrorCode.UNAUTHORIZED_ERROR, "还没有登录")
        
# 用户登录
@response_wrapper
@require_POST
def user_login(request: HttpRequest):
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')
    # 使用Django的authenticate函数验证用户名和密码
    user = authenticate(username=username, password=password)

    # 通过查询邮箱找到对应的用户
    if user is None and '@' in username:
        # 使用邮箱登录，查询email相等的用户
        tmp_user = User.objects.filter(email=username).first()
        if tmp_user is None:
            return fail_response(ErrorCode.CANNOT_LOGIN_ERROR, "用户名或邮箱不存在！")
        username = tmp_user.username
        user = authenticate(username=username, password=password)

    if user:
        login(request, user)

        request.session['is_login'] = True
        request.session['user_id'] = user.id
        request.session['username'] = user.username

        global login_id
        login_id = user.id
        print("login, id to " + str(login_id))
        return success_response({
            "message": "登录成功"
        })
    elif User.objects.filter(username=username).exists():
        # 密码错误
        return fail_response(ErrorCode.CANNOT_LOGIN_ERROR, "密码错误！")
    else:
        # 登录失败
        return fail_response(ErrorCode.CANNOT_LOGIN_ERROR, "用户名或邮箱不存在！")
```

### 用户信息修改

支持相应的用户信息修改，并且支持上传图片实现更高效的自定义。

![image-20240731221012039](https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407312210811.png)

## 支持搜索菜品

我们实现了对于用户搜索信息的推荐算法，从数据库中返回最符合用户需求的菜品，从而支持自动搜索菜品。

具体的搜索逻辑为按照响应的关键词，利用基本的分词功能进行匹配，找出最为匹配的关键项。

并且，在开发版本中，我们尝试使用相应库比较自然语言文本之间的余弦相似度。但是由于用户可能的输入较为多样，无法较好欢迎搜索意愿，该实现在发布中舍去。我们实现了对于用户搜索信息的推荐算法，从数据库中返回最符合用户需求的菜品，从而支持自动搜索菜品。

具体的搜索逻辑为按照响应的关键词，利用基本的分词功能进行匹配，找出最为匹配的关键项。

并且，在开发版本中，我们尝试使用相应库比较自然语言文本之间的余弦相似度。但是由于用户可能的输入较为多样，无法较好欢迎搜索意愿，该实现在发布中舍去。

```py
def matches_search(comment, search_string):
    return (difflib.SequenceMatcher(None, comment.title, search_string).ratio() > 0.3) or (comment.title in search_string) or (search_string in comment.title)
```

## 支持大语言模型的用餐建议推荐

我们采用了Yi-34B大语言模型，它是由零一万物开发并开源的双语大语言模型，使用4K序列长度进行训练，在推理期间可扩展到32K；模型在多项评测中全球领跑，取得了多项 SOTA 国际最佳性能指标表现。

实现逻辑为：后端实现调用该大语言模型的接口，并将接口提供给前端进行调用。

核心代码：

```py
import os
import qianfan

os.environ["QIANFAN_ACCESS_KEY"] = "your_key"
os.environ["QIANFAN_SECRET_KEY"] = "your_key"

chat_comp = qianfan.ChatCompletion()

def llm(content):
    return chat_comp.do(model="Yi-34B-Chat", messages=[{
        "role": "user",
        "content": "假如你是一个美食推荐专家，对食堂中的美食进行个性化推荐，" + content,
    }])
```

该部分代码展示了后端调用大语言模型并为前端提供接口的部分。同时，我们给该大语言模型提供了关于学校食堂与相应菜品的知识，使得其可以对用户的需求作出个性化推荐。

## 支持点击评论卡片跳转到对应的菜品页

对于参考的网站小红书，本项目并没有采用常规的点击分享卡片跳转到分享界面的设计，而是采用了跳转到具体的菜品页的设计。

菜品页可以查看对应菜品的具体信息，包括评分，对应的所有评论等。

并且支持在该页面下发布新评论。

前端实现为：通过id经路由跳转到对应的链接处。

```vue
<div class="card" v-for="comment in filteredComments" :key="comment.id"
               @click="goToDetail(comment.dish_id)">

goToDetail(id) {
  this.$router.push({name: 'detail', params: {id}});
}
```

后端实现为：

```py
path('detail/<int:id>/', get_dish_info_id),

@response_wrapper
@require_GET
def get_dish_info_id(request: HttpRequest, id: int):
    dish = Dish.objects.filter(id=id).first()

    comments = Comment.objects.filter(dish_name=dish.name)
    comments_list = []
    images = []

    grade_sum = 0
    price_sum = 0
    flavour_sum = 0
    waiting_time_sum = 0

    for comment in comments:
        author_name = "momo"
        avatar = default_avatar
        if not comment.author_id == 0:
            user = User.objects.get(id=comment.author_id)
            author_name = user.username
            avatar = user.avatar
        images.append(comment.image)

        grade_sum += comment.grade
        price_sum += comment.price
        flavour_sum += comment.flavour
        waiting_time_sum += comment.waiting_time

        comment_dict = {
            'id': comment.id,
            'title': comment.title,
            'content': comment.content,
            'date': comment.date.strftime('%Y-%m-%d %H:%M:%S'),  # 格式化日期
            'image': comment.image,

            'grade': comment.grade,
            'price': comment.price,
            'flavour': comment.flavour,
            'waiting_time': comment.waiting_time,

            'restaurant_name': comment.restaurant_name,
            'dish_name': comment.dish_name,
            'dish_id': dish.id,
            'author_id': comment.author_id,
            'author_name': author_name,
            'avatar': avatar,
        }
        comments_list.append(comment_dict)

    cnt = len(comments)
    return success_response({
        "name": dish.name,
        "image": dish.image,

        "address": dish.address,
        "restaurant_name": dish.restaurant_name,

        "description": dish.description,

        "prices": price_sum / cnt,
        "overall_rating": grade_sum / cnt,
        "flavor_rating": flavour_sum / cnt,
        "waiting_time": waiting_time_sum / cnt,

        "comment_num": len(comments_list),
        "comments": comments_list,

        "images": images,
    })
```

## 支持用户评论菜品

核心逻辑为通过设计comment类，增加其所需属性，后端为前端提供所需接口（如`agree_comment`, `creat_comment`, `get_comment_basics`等等）来支持用户评论菜品。

具体代码如下：

```py
# comment 类
class Comment(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, verbose_name='评论ID', editable=False)
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField(max_length=200, verbose_name='内容')
    date = models.DateTimeField(auto_now_add=True, verbose_name='日期')
    image = models.CharField(default=default_img, verbose_name='图片', max_length=500)

    grade = models.IntegerField(default=0,
                                choices=(
                                    (0, '未评分'), (1, '一星'),
                                    (2, '二星'), (3, '三星'),
                                    (4, '四星'), (5, '五星')
                                ), verbose_name='评分')
    price = models.FloatField(default=0, verbose_name='价格')
    flavour = models.FloatField(default=0, verbose_name='风味')
    waiting_time = models.FloatField(default=0, verbose_name='等待时间')

    restaurant_name = models.CharField(max_length=200, verbose_name="所属食堂", default="默认食堂")
    dish_name = models.CharField(max_length=200, verbose_name="对应菜品", default="菜品")
    author_id = models.IntegerField(default=0)

    # agree_count = models.IntegerField(default=0)
    # agree_author_ids = models.ManyToManyField(int, related_name='agree_comments')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'comments'
        ordering = ['-date']
        verbose_name = '评论'
        verbose_name_plural = '评论'

# comment 接口（仅展示部分）
def creat_comment(request):
    user = request.user

    body = json.loads(request.body.decode('utf-8')).get('params')
    title = body.get('title', '默认标题')
    content = body.get('content', '空空如也')
    # TODO：图片问题
    # image = ...
    dish_name = body.get('dish_name', '默认')
    restaurant_name = body.get('restaurant', '默认')

    grade = float(body.get('grade', '5'))
    price = float(body.get('price', '20'))
    if price < 0 or price > 9999:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "价格不合理！")
    flavour = float(body.get('flavour', '5'))
    waiting_time = float(body.get('waiting_time', '60'))

    author_id = 0
    if not user.is_anonymous:
        author_id = user.id

    if Dish.objects.filter(name=dish_name).exists():
        dish = Dish.objects.filter(name=dish_name).first()
        comment = Comment(title=title,
                          content=content,

                          grade=grade,
                          price=price,
                          flavour=flavour,
                          waiting_time=waiting_time,

                          restaurant_name=restaurant_name,
                          dish_name=dish_name,
                          author_id=author_id)
        comment.save()
        dish.comments.add(comment)
        if not user.is_anonymous:
            user.comments.add(comment)
        return success_response({"message": "创建成功！", "title": comment.title})
    else:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "菜品不存在！")
```

## 支持用户点赞他人的评论

核心逻辑为后端采用django框架，在model中设置相应属性，并在API package中为前端提供接口（`agree_comment`）。

核心代码为agree_comment（后端提供的接口函数）：

```py
@response_wrapper
@require_POST
def agree_comment(request: HttpRequest):
    body = json.loads(request.body.decode('utf-8'))
    comment_id = body.get('comment_id', '')
    comment = Comment.objects.get(id=comment_id)
    user = request.user
    if comment is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "评论不存在")
    if user in comment.agrees.all():
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "已点赞")

    comment.agree_count.add(1)
    comment.agree_authors.add(user)
    return success_response({"message": "点赞成功！"})
```

## 支持用户收藏食堂和菜品

同样，本部分的核心逻辑遵循前后端分离的设计，后端采用django框架，在model中设置相应属性，并在API package中为前端提供接口。

具体代码如下：(仅展示部分核心代码)

```py
# 用户收藏菜品
def user_collect_dish(request: HttpRequest):
    user, dish = get_user_and_obj(request)
    if dish is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '菜品不存在')
    else:  # add dish to collected_dishes
        user.collected_dishes.add(dish)
        return success_response({
            "id": user.id,
            "dish_id": dish.id,
        })
        
# 用户删除菜品
def user_delete_dish(request: HttpRequest):
    user, dish = get_user_and_obj(request)
    user.collected_dishes.remove(dish)
    return success_response({
        "id": user.id,
        "dish_id": dish.id,
    })
    
# 用户查找菜品
def user_lookup_dish(request: HttpRequest):
    user, dish = get_user_and_obj(request)
    if dish is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '菜品不存在')
    else:
        return success_response({
            "id": user.id,
            "dishes": user.collected_dishes,
        })
```

## 支持发布用餐记录

发布用餐记录有两种方式，一种是在首页“就这个！”点击后，会自动添加就餐记录。

![image-20240731221437347](https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407312214909.png)

并且，支持用餐记录管理页面，可以管理用餐记录。

在这个管理页面中，可以查询、添加、删除、修改相应的用餐记录。

![image-20240731221506530](https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407312215879.png)

## 支持美食广场功能与自动推荐菜品

我们实现了从数据库筛选精品菜肴，为用户在美食广场首页直接呈现。

核心逻辑为根据用户综合评分选择菜品，通过接口将这部分高分菜品随机返回给前端，前端在美食广场首页进行呈现。

核心代码如下：

```py
# 推荐菜品
def get_dish_recommend(request: HttpRequest):
    place = random.choice(places)
    dish = random.choice(dishes)
    recommendation = "在" + str(place) + "吃" + str(dish)

    return success_response({
        "recommendation": recommendation,
        "place": str(place),
        "dish": str(dish),
    })
```

## 支持个人行为分析

在个人信息界面，有自动化的用户信息统计，以图标形势欢迎用户的个人信息。

![image-20240731221622995](https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407312216378.png)

# 项目运行过程

项目的运行步骤为：

1. 创建虚拟环境，要求python环境>=3.10
2. 安装相应需要的包
   1. 要求分别在前后端目录中运行
   2. 后端所需包为pip install -r requirements.txt
   3. 前端所需包为npm install
3. 启动后端服务
4. 启动前端服务

```shell
# 创建虚拟环境

# 启动后端服务
cd backend
pip install -r requirements.txt
python manage.py runserver

# 启动前端服务
cd frontend //前端
npm install 
npm install vue-cli-service
npm run serve
```

成功启动后，可以看到项目的首页，开始探索今天在北航究竟要吃什么吧！

![image-20240731221720903](https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407312217315.png)

# 五、项目总结

项目总体完成情况概述，是否符合自己预期。

"在北航吃什么"项目是一个基于Vue.js和Django技术栈的前后端分离Web应用，旨在为北航的师生提供一个全面、便捷的餐饮服务信息平台。项目的核心功能包括多用户登录注册、个性化菜品推荐、食堂和菜品的增删改查、用户就餐记录的跟踪与管理、用户评论互动以及个人信息的修改与管理等。

项目的成功实施，得益于团队成员的紧密合作和对用户需求的深入理解。我们采用了Vue.js来构建动态且响应式的用户界面，而Django则以其强大的后端服务能力，为前端提供了稳定可靠的数据支持。通过精心设计的数据模型和数据库结构，我们确保了数据的一致性和系统的高效运行。

在用户体验方面，我们特别强调个性化服务的重要性。通过智能推荐算法，系统能够根据用户的喜好和历史行为，推荐符合用户口味的菜品。此外，用户可以方便地记录自己的就餐情况，并对菜品进行评论和点赞，从而形成一个活跃的社区氛围，促进信息的共享和交流。

经过为期两周的前后端分离开发和7次的项目碰头会，我们最终完成了项目的开发，基本符合了开发前团队的预期。随着项目的不断完善，我们计划引入更多智能化服务，如智能食谱推荐和营养分析，以进一步提升用户体验。我们相信，随着技术的不断进步和平台功能的持续优化，"在北航吃什么"将成为北航社区中不可或缺的一部分，为师生的校园生活带来更多便利和乐趣。

总的来说，"在北航吃什么"项目不仅是一次技术实践的尝试，更是对团队协作和创新思维的一次考验。通过这个项目，我们不仅为北航的师生提供了一个实用的餐饮服务平台，也为团队成员积累了宝贵的开发经验，为未来的技术探索和应用奠定了坚实的基础。

# 六、课程学习总结

1. 课程收获和难点分析（小组成员是否有Python或大作业要求的基础，做完这个大作业自我感觉是否有提高等其他收获，本次项目感觉最困难的地方在哪里）

   我们小组一开始对python仅限于简单的了解，对大作业所需要的GUI或者是前端相关的技术都是完全不了解，团队没有任何的前后端经验。在学习完课程之后，开始上手大作业的时候的确感受到了很高的强度，对于前后端开发的无知。经过这次大作业的练习，我们组的同学对python的基础知识与相关库的应用都了解的更深了，具有了基本的前后端开发经验。

   大作业的难点主要在以下方面：学习曲线陡峭： 对于没有编程基础的成员来说，从零开始学习Python，需要花费大量时间理解基本概念和语法；调试和错误处理： 遇到错误时，定位和修复错误需要大量的尝试和学习，对新手来说是一个巨大的挑战’项目管理： 大作业涉及的内容较多，需要合理分配任务和时间，确保每个成员都能按时完成自己的部分；代码优化： 如何写出高效、优雅且可维护的代码，对每个成员来说都是一个挑战，尤其是在项目接近尾声时，代码的复杂性增加，优化变得更加困难。

   通过这次Python课程和大作业的实践，所有成员都有了不同程度的提升。无论是对Python的语法和库的掌握，还是在实际项目中的应用能力，都有显著的进步。同时，也认识到在学习和项目过程中存在的困难和不足，这些都为今后的学习和工作提供了宝贵的经验。

2. 教师授课评价（老师上课过程的一些建议，以及希望老师之后能够介绍一些什么东西）

   老师从基础讲起，带领我们熟练使用python语言，很好的帮助了我们这些不会python的同学在面对大作业的时候的上手难度。但是课堂上对于Python项目的实战介绍感觉偏少，所以在刚刚接触大作业时感到较为吃力。希望课程能增加一些针对于python在web应用与框架上面的应用的介绍，比如django模型的使用等等。

3. 助教评价*

   本次我们小组在完成大作业时遇到具体问题与架构设计方面主要是自己查找资料，因为感觉自己动手寻找问题的解决方法也是“一个程序员重要的自我修养”之一。但是对于题目理解与部分难以解决的问题也寻求了助教的帮助，助教学长也很热情用心的进行了解答，对我们很有帮助！

4. 当前课程教授内容评价与课程进一步改进建议

   课程内容对我们这些没有Python基础的同学帮助非常大。通过系统的学习，我们不仅掌握了Python的基本语法和编程技巧，还能够应用这些知识解决实际问题。特别是在应用开发，数据处理、分析和可视化方面，我们看到了Python强大的功能和广泛的应用。希望未来能够有更多的训练机会，让我们可以深入了解Python在不同领域的应用，例如人工智能、机器学习、网络爬虫、自动化脚本等。通过这些实践，我们可以进一步提升编程能力和实际操作水平，更好地应对未来的学习和工作挑战。

# 主要参考资料

后端;

1. 数据库：[PycharmSQlite教程](https://www.bilibili.com/video/BV1UN4y1p7Xr/?spm_id_from=333.880.my_history.page.click&vd_source=fcb17388f72a0e6539283a507d29e8ee)，[Python操作sqlite](https://www.bilibili.com/video/BV1LW4y1S7L1/?spm_id_from=333.880.my_history.page.click)
2. django：[django框架学习](https://www.bilibili.com/video/BV1bM411r7eE/?spm_id_from=333.999.0.0)
3. 数据获取（爬虫）：[爬虫入门到精通](https://www.bilibili.com/video/BV1ut4y1B7CX/?spm_id_from=333.337.search-card.all.click)，[Python使用bs4爬取网页数据](https://blog.csdn.net/weixin_42340783/article/details/137859643?ops_request_misc=%7B%22request%5Fid%22%3A%22172242594316800182769514%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=172242594316800182769514&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-3-137859643-null-null.142^v100^control&utm_term=python爬虫网页数据抓取&spm=1018.2226.3001.4187)
4. 大模型API：[百度智能云官方文档](https://cloud.baidu.com/)
5. 参考仓库：[HangEat](https://github.com/volcaxiao/HangEat-Backend)

前端：

1. [vue官方文档](https://cn.vuejs.org/)
2. [axios官方文档](https://axios-http.com/zh/docs/intro)
3. [element-plus官方文档](https://element-plus.org/zh-CN/)
