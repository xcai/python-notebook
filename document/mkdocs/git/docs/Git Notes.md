# Git Notebook

###  下载路径
---
    ==.git/config==找到下载的路径URL
---
#### Git查看远程仓库地址
```
git remote -v
```
---
git diff的时候忽略换行符的差异
```
git config --global core.whitespace cr-at-eol
```
### Git删除文件及清除其所有日志记录
```
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch Remove_file_path' --prune-empty --tag-name-filter cat -- --all
```

---
```
git stash save 'message...' #保存当前工作进度，会把暂存区和工作区的改动保存起来
git stash list    # 显示保存进度的列表
git stash pop     # 恢复最新的进度到工作区，并删除stash
git stash apply   # 缓存堆栈中的stash多次应用到工作目录中，但并不删除stash拷贝
git stash clear   # 删除所有存储的进度。
```
---
#### Git diff ^M的消除
```
git config --global core.whitespace cr-at-eol
```

---
#### 查询git国内DNS
>  https://www.ipaddress.com/
```
192.30.253.112 github.com   
192.30.253.118 gist.github.com   
185.199.111.153 assets-cdn.github.com   
151.101.185.194 github.global.ssl.fastly.net  
```
```
# GitHub Start
151.101.100.133 assets-cdn.github.com
192.30.253.112 github.com
192.30.253.118 gist.github.com
185.199.111.153 assets-cdn.github.com
151.101.185.194 github.global.ssl.fastly.net
151.101.184.133 raw.githubusercontent.com
151.101.112.133 gist.githubusercontent.com
151.101.184.133 cloud.githubusercontent.com
151.101.112.133 camo.githubusercontent.com
151.101.112.133 avatars0.githubusercontent.com
151.101.112.133 avatars1.githubusercontent.com
151.101.184.133 avatars2.githubusercontent.com
151.101.12.133 avatars3.githubusercontent.com
151.101.12.133 avatars4.githubusercontent.com
151.101.184.133 avatars5.githubusercontent.com
151.101.184.133 avatars6.githubusercontent.com
151.101.184.133 avatars7.githubusercontent.com
151.101.12.133 avatars8.githubusercontent.com
52.216.161.227 github-production-release-asset-2e65be.s3.amazonaws.com
# GitHub End
```
---

---
#### git 使用代理proxy解决网速慢问题：
创建~/.gitconfig文件，写入：
```
[http]
    proxy = socks5://10.10.10.21:1080
[https]
    proxy = socks5://10.10.10.21:1080" > .gitconfig
```
##### windows:
在`C:\Users\89155\.ssh`目录下建立`config`文件，内容为
```
ProxyCommand connect -S 127.0.0.1:1080 -a none %h %p

Host github.com
  User git
  Port 22
  Hostname github.com
  # 注意修改路径为你的路径
  IdentityFile "D:\ProgramsData\id_rsa_1024"
  TCPKeepAlive yes

Host ssh.github.com
  User git
  Port 443
  Hostname ssh.github.com
  # 注意修改路径为你的路径
  IdentityFile "D:\ProgramsData\id_rsa_1024"
  TCPKeepAlive yes
```

---
##### 设置代理：
```
git config --global https.proxy http://127.0.0.1:1080
git config --global https.proxy https://127.0.0.1:1080
```
##### 取消代理：
```
git config --global --unset http.proxy
git config --global --unset https.proxy
```
---

###### 去除右键Git init here，Git Gui，Git Bash
```
cmd进入C:\Program Files (x86)\Git\git-cheetah，
执行 regsvr32 /u git_shell_ext64.dll

```

---


###### 存储：
* git/refs/head/[本地分支]
* git/refs/remotes/[正在跟踪的分支]
* 

---
Git使用https方式进行连接时，默认每次推送时都要输入用户名和密码。可以使用命令:
```
git config credential.helper store
```
为当前仓库设置记住密码，设置后，只要在推送一次，以后就不需要用户名和密码了。   
自己设置时间，可以这样做:
>     git config credential.helper 'cache --timeout=3600'

---
##### [Git log](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%80%89%E6%8B%A9%E4%BF%AE%E8%AE%A2%E7%89%88%E6%9C%AC):

1. 所有的提交记录：  
> git show   
> git log --pretty=format:"%h %an   %s"

2. 通过sha-1查看某个log记录
>       git show [sha-1]

3. Git 可以为 SHA-1 值生成出简短且唯一的缩写。 如果你在 git log 后加上 --abbrev-commit 参数，输出结果里就会显示简短且唯一的值；默认使用七个字符，不过有时为了避免 SHA-1 的歧义，会增加字符数:
>       git log --abbrev-commit --pretty=oneline 

4. **引用日志**：当你在工作时， Git 会在后台保存一个引用日志(reflog)，引用日志记录了最近几个月你的 HEAD 和分支引用所指向的历史，查看引用日志：
>       git reflog

5. 怎样获取git最近一次commit的sha-1缩写:
>       git log --pretty=format:"%h" -1
==-1==限制 log 的輸出範圍, ==-1==为输出一个，==-2==就输出两个
format选项| 选项说明
---|---
%H 	|該更新的SHA1雜湊值
%h 	|該更新的簡短SHA1雜湊值
%T 	|存放該更新的根目錄的Tree物件的SHA1雜湊值
%t 	|存放該更新的根目錄的Tree物件的簡短SHA1雜湊值
%P 	|該更新的父更新的SHA1雜湊值
%p 	|該更新的父更新的簡短SHA1雜湊值
%an |	作者名字
%ae |	作者電子郵件
%ad |	作者的日期 (格式依據 date 選項而不同)
%ar |	相對於目前時間的作者的日期
%cn |	提交者的名字
%ce |	提交者的電子郵件
%cd |	提交的日期
%cr |	相對於目前時間的提交的日期
%s 	|標題




##### git 文件归档（export）
- 基于最新提交建立归档文件latest.zip：

>        git archive -o latest.zip HEAD

---
#### 在本地仓库添加一个远程仓库,并将本地的master分支跟踪到远程分支
> git remote add origin git@github.com:xcai/captain_s.git   

> git pull origin master  

> git push origin master

---
#### Git pull 强制拉取并覆盖本地代码
```
git fetch --all
git reset --hard origin/master
git pull
```
### Git更新同步push新建的repo
``` shell
git remote add origin git@github.com:xcai/deploy-aegis-doctor.git
git push -u origin master
```

---

---
#### 丢弃工作区的修改
```
git checkout -- <file>...        to discard changes in working directory
```
#### 把暂存区(git add等文件）的修改撤销掉（unstage），重新放回工作区
```
git reset HEAD <file>
```

#### 对所有文件都取消跟踪
```
git rm -r --cached . 　　//不删除本地文件
git rm -r --f . 　　//删除本地文件
```
#### 对某个文件取消跟踪
```
# 删除readme1.txt的跟踪，并保留在本地。
git rm --cached readme1.txt   

# 删除readme1.txt的跟踪，并且删除本地文件。
git rm --f readme1.txt    
```
---

#### 执行完commit后，撤销commit
```
git reset --soft HEAD^
```
HEAD^的意思是上一个版本，也可以写成**HEAD~1**
如果你进行了2次commit，想都撤回，可以使用**HEAD~2**
##### --mixed
> 不删除工作空间改动代码，撤销commit，并且撤销git add . 操作
这个为默认参数,git reset --mixed HEAD^ 和 git reset HEAD^ 效果是一样的。
#### --soft
> 不删除工作空间改动代码，撤销commit，不撤销git add . 
#### --hard
> 删除工作空间改动代码，撤销commit，撤销git add . 

##### commit注释写错,修改注释
```
git commit --amend
```
此时会进入默认vim编辑器，修改注释完毕后保存就好了。

---
### git 通过[vimdiff](https://www.jianshu.com/p/5e359ac7d609)完成了conflict的手动合并
```
git mergetool
```