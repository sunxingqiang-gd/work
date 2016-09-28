# GeneDock 发布日志撰写规范

GeneDock的[发布日志](https://genedock.com/logs/)既可以告知用户我们的功能更新，也可以记录系统的迭代过程。故，撰写此文档，阐述和规范一下发布日志的撰写方式。

## 整体步骤

1. 撰写md文档，还要写[yaml头文件](http://jekyllrb.com/docs/frontmatter/)
2. 开issue，建branch，(具体的git操作参考文后操作)，向frontline的[gdlogs分支的`WebServer/gdlogs/source/_posts`目录](https://github.com/genedock/frontline/tree/gdlogs/WebServer/gdlogs/source/_posts)，提交pr
3. 若pr合并，则可邮件通知前端（主要是李大明）和产品经理（荣惠），申请上线发布日志

## md文档撰写方式

- md文档开始的yaml头文件

```yaml
---
layout: postc       # 此处固定写postc
title: 标题          # 此处写文档的标题
date: 日期时间        # 此处写文档发布的日期
author: GeneDock     # 此处固定写GeneDock
---
```

- md文档正文

文档的第一行，会被当做缩略描述。其他的与正常的markdown撰写方式无异。

- 文件名

文件名使用日期开头，格式8个数字，不支持中文命名。例如`20160920-public-tool-release-1.md`


## 示例

- 示例md文档

```
---
layout: postc
title: 公共工具新增转录组相关工具
date: 2016-09-22 10:29:22
author: GeneDock
---
公共工具新增转录组相关工具

主要更新：

- 质控工具，RSeQC_bam-stat、RSeQC_geneBody-coverage、RSeQC_inner-distance、RSeQC_junction-saturation、RSeQC_read-distribution。
- 组装工具，Cufflinks和Cuffmerge。
- 差异表达基因工具，RSEM_Calculate_Expression和RSEM_Prepare-Reference。
- 融合蛋白工具，Tophat2_tophat-fusion。

您可以在“工具”页面中查看他们的描述、输入/输出/参数项等详细信息。

```

- 最终结果

![示范图](http://ww2.sinaimg.cn/large/a9c2d1f2jw1f86us8yooij20t90j6n0h.jpg)

## git用于拉远端分支的几个命令和提交PR

- `git branch -a`,`-a`参数是列出所有远端和本地分支
- `git checkout origin/<远端分支名>`，切到某个远端分支
- `git checkout -b <远端分支名>`，从远端的分支，新建一个与远端分支名相同的本地分支
- `git checkout -b issue#xxx`，从<远端分支名>再checkout一个任务issue分支，在此issue上进行增加文档，用来和<远端分支名>进行比较
- `git add -f`，由于为防止提错分支，到master上，所以该目录下的文件被放到了`.gitignore`中，故需要使用`-f`参数

### 注意
提交PR的时候，要将issue#xxx与gdlogs的分支进行比较，不要和master的分支进行比较
