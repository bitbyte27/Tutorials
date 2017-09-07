## Git Bash
1. cd 文件目录
2. git add 文件名.扩展名
3. git commit -m '更改的提示'
4. git push origin master
5. 输入GitHub密码
* 对于更改一个文件，这个方式是不错的，但多个文件，每个都要add→commit，那就耗死了，<del>还在摸索更好的方法。</del>此时你可以使用 . （一个小数点）表示当前目录，或者使用 * （一个星号）表示目录下所有文件，或者使用 git add 的 -A 参数（POSIX 风格）或者 --all 参数（GNU 风格），甚至使用 Glob 以表示还不至于整个目录的大量文件。
* <ins>如果没有任何新增的文件的话，可以省略 git add，转而在 commit 阶段添加 -a 参数</ins>
* <ins>原作者没有使用过 SSH 方式吧估计</ins>
* 文件名、文件目录尽量不要有空格，有空格的文件目录用单引号括起来，如：cd ‘Pattern Recognition’。<br>

![png](git_cd.png)
