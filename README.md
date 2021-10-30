# qinglong_auto_tools

自用工具，写的烂勿喷。

目录结构：

| 文件名字 | 用途 |
|  ----  | ----  |
| 2288 | 2.2和2.8青龙批量上传ck脚本 |
| Script | 个人修改的一些py脚本，自用，勿喷 |
| qq | qq相关脚本，自用 |
| tg | tg相关脚本，自用 |
| trs_stream.py | 本地转换stream抓到的headers为json格式，使用方法详见注释 |
| ck_auto_select.py | ck本地去重小工具，用法看注释 |  
| cks_push_alql.py | 多容器ck分发工具，方便多容器管理，用法详见注释 |
| cks_merge_alql.py | 多容器ck合并工具，方便多容器管理，用法详见注释 |
| cks_sync_able.py | 多容器同步环境变量启用禁用脚本，方便多容器管理，使用方法详见注释 |
| tasks_sync_able.py | 多容器同步任务启用禁用脚本，方便多容器管理，使用方法详见注释 |
| tasks_sync_scripts_able.py | 多容器同步已启用的脚本文件，方便多容器脚本更新管理，使用方法详见注释 |
| tasks_sync_all.py | 多容器无脑同步所有脚本文件和任务，方便多容器脚本迁移管理，使用方法详见注释 |
| scripts_check_nets.py | 单容器查询自己脚本文件中的网络链接，查询脚本中含有的链接，使用方法详见注释 |
| scripts_purge_keys.py | 单容器清除屏蔽词脚本，屏蔽脚本中含有的屏蔽词，使用方法详见注释 |
| ec_config.txt | 多容器脚本和单容器脚本的配置文件，请按照脚本提示填写 |


### 多容器相关脚本 

仅支持云服务器部署的2.9.0以上的青龙

| 文件名字 | 用途 |
|  ----  | ----  |
| ec_config.txt | 多容器脚本和单容器脚本的配置文件，请按照脚本提示填写 |
| cks_push_alql.py | 多容器ck分发工具，方便多容器管理，用法详见注释 |
| cks_merge_alql.py | 多容器ck合并工具，方便多容器管理，用法详见注释 |
| cks_sync_able.py | 多容器同步环境变量启用禁用脚本，方便多容器管理，使用方法详见注释 |
| tasks_sync_able.py | 多容器同步任务启用禁用脚本，方便多容器管理，使用方法详见注释 |
| tasks_sync_scripts_able.py | 多容器同步已启用的脚本文件，方便多容器脚本更新管理，使用方法详见注释 |
| tasks_sync_all.py | 多容器无脑同步所有脚本文件和任务，方便多容器脚本迁移管理，使用方法详见注释 |

青龙拉取命令：

环境变量相关：

```bash
ql repo https://ghproxy.com/https://github.com/spiritLHL/qinglong_auto_tools.git "cks_"
```

任务相关：

```bash
ql repo https://ghproxy.com/https://github.com/spiritLHL/qinglong_auto_tools.git "tasks_"
```

### 单容器相关脚本

仅支持云服务器部署的2.9.0以上的青龙

| 文件名字 | 用途 |
|  ----  | ----  |
| ec_config.txt | 多容器脚本和单容器脚本的配置文件，请按照脚本提示填写 |
| scripts_check_nets.py | 单容器查询自己脚本文件中的网络链接，查询脚本中含有的链接，使用方法详见注释 |
| b_scripts_purge_keys.py | 单容器清除屏蔽词脚本，屏蔽容器脚本中含有的屏蔽词，使用方法详见注释 |

屏蔽脚本暂时有bug，别用

青龙拉取命令：

```bash
ql repo https://ghproxy.com/https://github.com/spiritLHL/qinglong_auto_tools.git "scripts_"
```

### 容器相关脚本使用说明(小白必看)

脚本使用：

#### 1.先说环境变量相关

成功使用ql命令拉环境变量相关脚本取后，在”青龙“里使用脚本管理右上角新建文本，命名"ec_config.txt"，然后在里面粘贴本仓库对应文件的内容，按照注释填写信息，然后保存，注意对应变量！！！

![脚本管理图](https://i.loli.net/2021/10/29/cyK9R8IwjP1WA7U.png)

ps:别在服务器里创建并修改ec_config.txt文件，青龙识别不到没用的，一定要用青龙的“脚本管理”创建并填写信息！！！

#### 2.脚本 cks_push_alql.py，也就是任务 二叉树分发ck ，会从主青龙里取出不含wskey的ck，按顺序转发到副的容器(青龙)里，每个容器默认35个号，最后会整合所有不含wskey的ck，转发到备份容器(青龙)里，备份容器(青龙)就是主青龙没有wskey的副本。

![分发效果图](https://i.loli.net/2021/10/29/25LarSXgqpTKPs6.png)

该脚本分发不识别是否启用禁用ck！默认全转发(含禁用的)！如若其余的青龙(容器)没有对应pin值的ck，会自动添加到该容器(青龙)的环境变量最后！

第一个副青龙(容器)里使用任务相关脚本，统合管理其余的副青龙(容器)，这个后面再说怎么配置。

副青龙(容器)专门拿来跑不需要互助，或者互助人数少的脚本。备份容器(青龙)是单独的容器，专门拿来跑需要所有ck的脚本。

第一次运行分发脚本运行后，转发到其他容器(青龙)后，其他容器(青龙)的ck位置可以手动调整，下次分发到其他容器(青龙)时，ck不会改变你调整的位置。这个规律也适用于备份容器(青龙)，第一次分发后再调整备份容器(青龙)的ck位置，后面再分发不会改变位置！

#### 3.脚本 cks_sync_able.py，也就是 二叉树环境变量状态同步 ，会同步ck的状态，同步ck启用禁用情况，在 二叉树分发ck 后使用。

ps:该脚本暂时有bug，同时会更新环境变量的值(含wskey)，有时间我修补好了再使用吧，现在先禁用！！！

顺序上来说，主青龙的脚本运行顺序应该是 转ck 早于 分发ck 早于 ~~环境变量状态同步（暂时别用，有bug）~~ 

#### 4.主青龙配置完毕，该配置跑脚本的第一个副青龙(容器)了

“跑脚本的第一个副青龙(容器)”成功使用ql命令拉取任务相关后，在”青龙“里使用脚本管理右上角新建文本，命名"ec_config.txt"，然后在里面粘贴本仓库对应文件的内容，按照注释填写信息，然后保存，注意对应变量！！！

配置好"ec_config.txt"后，就能使用对应脚本了。注意，这里的任务相关的脚本配置，主青龙是指的是跑脚本的第一个容器，不是前面环境变量相关的那个拿来转码的主青龙，这一点别搞混了。

看到这里，如果你同步脚本的其他青龙不是空容器，事先有跑过脚本，那么下面这几行字就不用看了，看步骤5去吧，下面是给空容器(青龙)准备的。

首先，如果你是给空容器同步，第一次使用的应该是 tasks_sync_all.py ，也就是 二叉树无脑同步 。该脚本会无脑同步你配置的第一个副青龙(容器)到别的容器(青龙里)。

它会自动给空容器添加脚本和对应任务，忽略脚本是否被禁用的同步。这个操作只能运行“一次”，多次运行会多次添加任务的，所以别重复运行，任务相关的日常使用的脚本只有步骤5那两个。

如果是空容器，运行完上一步后，除了以文件夹形式存储的依赖，都应该已经同步了，注意那些npm和python依赖还是得命令行装，因为脚本不会同步这些东西。

#### 5.跑脚本的第一个副青龙(容器)需要必装的两个脚本

tasks_sync_scripts_able.py 和 tasks_sync_able.py。它们分别是 二叉树同步脚本文件 和 二叉树同步任务启用禁用 。

脚本运行顺序是先同步文件，再同步任务启用禁用。注意这里的两个脚本对应主青龙(容器)是跑脚本的第一个容器(青龙)，不是转码那个。

粗略解释一下运作原理，首先从主青龙中取得启用任务对应的脚本，然后检索被同步的其他青龙，如果已有的(任务对应的)脚本有更改，会把脚本更改同步到其他青龙里去。

如果任务不存在，会自动新增任务和对应脚本，检索判断是 名字+命令+定时 是否有相同的存在，不存在就会新增，存在就只检索脚本是否有区别需要更新。

二叉树同步任务启用禁用 这个任务则会检索青龙(容器)，同步任务的状态，是启用还是禁用。(这里的检索条件是任务名字，如果有相同名字，可能无法同步)

#### 6.接下来说说单文件脚本

相信经过上面的配置，应该懂怎么配置了，注意配置对应的注释和变量，别填错地方就行。

scripts_check_nets.py ，也就是 二叉树查网络链接 ，配置好后运行会查询仓库脚本的网络链接，还有其中含有屏蔽词的有几个，有需要可以试试。

清除屏蔽词的另一个脚本暂时有bug，有时间我修好再用吧，现在你们应该拉不到，忽略它。

最后贴个效果图吧。

![](https://i.loli.net/2021/10/30/m4eHKVof2A1SqbT.png)

![](https://i.loli.net/2021/10/30/gcsyT8Wa1QJmn2E.png)

![](https://sm.ms/image/hn84ya7pHKqfDTF)

暂时写到这，有时间再补充。

### 更新说明 

2021.10.30

更新 小白脚本使用说明

转载起码保留作者名谢谢


# 免责声明

* 代码仅供学习
* 不可用于商业以及非法目的,使用本代码产生的一切后果, 作者不承担任何责任.
