# 🫒Olive: A Multi-window Manager on macOS

![VperIw2](https://i.imgur.com/VperIw2.png)

固定模式演示：（与 Amethyst 同时使用）

![Title](https://github.com/Ryan-the-hito/Olive/blob/main/image/title.gif)

![J38IQ3F](https://i.imgur.com/J38IQ3F.gif)

随选模式演示：（与 Amethyst 同时使用）

![Show](https://github.com/Ryan-the-hito/Olive/blob/main/image/show.gif)

![bGhCYMI](https://i.imgur.com/bGhCYMI.gif)

## ℹ️基本介绍：

一键打开多个窗口（大于等于两个）的窗口管理工具。

普通情况下，如果我需要在 mac 上并置两个窗口，且当前桌面有大量窗口，我就需要一个一个最小化/隐藏，然后再找出我需要的两个窗口：

- 鼠标激活一个窗口为活动窗口
- 缩小这个窗口
- 鼠标激活另一个窗口为活动窗口
- 缩小这一个窗口
- 点击第一个我需要显示的窗口
- 点击第二个我需要显示的窗口

如此，当我多任务操作的时候，我就会非常精疲力尽。简单的同屏显示多个窗口，可能需要六步或者更多才能完成。而哪怕是 Stage Manager 也无法简单地“正选”出我想要同时显示的窗口——Stage Manager 需要多次拖拽操作。

我希望能这样操作：

- 打开选择界面
- 点选两个窗口

这样，将最大化和最小化的工作交给自动操作，除了我选择的窗口被显示之外，其他窗口自动隐藏。如果我可以这样操作，也许会轻松不少。

因此我打算做一个这样的软件——Olive。

## ⚙️下载使用：

1. 在 Release 里面找到最新的版本，下载，将解压的 .app 软件放入程序文件夹（Application）中。

   ![uRYuNsb](https://i.imgur.com/uRYuNsb.png)

2. 点击图标，启动软件，软件图标将在 Menu Bar 中显示。

3. 点击图标，就会弹出窗口选择界面，但是第一次使用的时候，应该还会弹出权限窗口，请给 Olive 提供 Accessibility 权限。（Olive 可以完全离线使用，不会对您的隐私带来任何影响）**关于更新：**更新时请在发布页面下载最新的软件打包并将其拖入程序文件夹替换原有软件。并且，由于 macOS 的限制，每次更新之后请再次授予 Olive 以Accessibility 权限。具体操作是：点击减号，将 Olive 从 Accessibility 的既有列表中移除，再点击加号，将 Olive 添加进入即可。

   ![4bI0Mtc](/Users/ryanshenefield/Downloads/4bI0Mtc.png)

4. 点击图标，选择“Start Olive”，此后，当切换窗口时，Olive 会每隔 5 秒左右检测正在运行的窗口（仅当前桌面**未**最小化/隐藏的窗口和所有桌面最小化/隐藏的窗口，不包括其他桌面**未**最小化/隐藏的窗口）并返回其标题。当你需要使用 Olive 的时候，点击图标（或者选单中的 “Select windows”）即可弹出窗口选择界面。选择界面将显示 20 个窗口，包括软件名称、窗口所在软件中的序号和窗口标题。每当你控制一个新软件的最大化和最小化时，mac 会弹出许可请求，请给予 Olive 这一权限。如果未授予这个权限，Olive 将无法正常运行。若在授权后 Olive 没有第一时间正确控制窗口，请再尝试一次，若仍无效，请考虑是否未将软件名称列入白名单（第 5 步），或考虑该软件无法被 AppleScript 控制（请移步“问题检查”）。

   ![WYKLhEk](https://i.imgur.com/WYKLhEk.png)

5. 一些**非常重要**的设置：点击“Settings”，将弹出如下界面：

   ![ck5eQ7r](https://i.imgur.com/ck5eQ7r.png)

   1. Number of side-by-side windows：这个表示你希望每次同时打开几个窗口。默认值是“2”，表示当你在窗口选择界面上点击了两个窗口之后，Olive 就会自动操作。如果是“3”，那么 Olive 将在你选择了三个窗口后自动操作。
      1. **固定模式：**如果在该框填入的数值大于 0，那么 Olive 将一直记忆您的使用习惯，默认您每次都将选择固定数值的窗口，在您**单击**了这一数值的窗口后会立即自动操作，如上所述。
      2. **随选模式：**您还可以在此处填入 0，进入随选模式。此时，您可以**单击**任选任何数值的窗口，只需在最后一个窗口上**双击**，Olive 就会立刻自动操作。例如，选择一个窗口需要**双击**该窗口；如果选择两个窗口，则在第一个窗口上**单击**，在第二个窗口上**双击**；若选择三个窗口，则在第一和第二窗口上**单击**，在第三个窗口上**双击**……以此类推。此模式的好处是可以随时选择任意数值的窗口，不受固定数值限制。

   2. Apps at running：这个列表显示了正在运行的软件名称。Olive 需要依赖这个去控制窗口的最小化和最大化等。请把你需要操作的软件名称复制到下面的列表中，请注意名称的准确性。
   3. Apps to control：**Olive 使用白名单控制窗口，只有你希望控制的软件才在 Olive 的控制之列。**因此请把上面列表中你希望的软件名称复制下来，一行一个，点击保存，最多五秒后即可在窗口选择界面上看到这个软件的窗口了。
   
   现在请愉快地多窗口操作吧！希望在繁重的多任务选择的时候会偶尔使用到 Olive！
   
   ![GJ9XNzY](https://i.imgur.com/GJ9XNzY.png)

## 💪进阶使用：

Olive 的设计是，当点击在 Menu Bar 上的图标的时候，就会显示弹出窗口选择界面，这样免去了在弹出的菜单中点击的麻烦。但是在一些 Macbook 上，Menu Bar 的空间不足以放下那么多图标，因此许多用户会使用隐藏图标的工具。如果图标被隐藏了，Olive 如何被唤起呢？Bartender 就提供了快捷键唤醒的方式，可以快速点选隐藏的图标。以下设置可供参考，当按下 Opt 和 ` 的时候，Bartender 就会点击已被隐藏了的 Olive 图标，窗口选择界面就会随之弹出。

![heIJYI1](https://i.imgur.com/heIJYI1.png)

另一个方法是使用 BetterTouchTool。如下图所示，可以将两指手势与点按图标的逻辑相结合，以两指在触控板上滑动触发窗口选择界面。（需要注意的是，如果使用这个方法，那么就不能隐藏 Olive 的图标，因为 BetterTouchTool 无法获取被隐藏了的图标信息。）

![gb94FYb](https://i.imgur.com/gb94FYb.png)

你还可以通过 Better Touch Tool 自定义 Hot Corner——当你的鼠标移动到屏幕的某个边角时，Olive 的选择面板就会自动弹出。

![QiQWHu6](https://i.imgur.com/QiQWHu6.png)

## ❓问题检查：

- **我用的设备是 M1 的电脑，所以好像我写的大部分软件只能在 Apple 芯片的电脑上运行。**
- （已解决）~~还有一定的 bug，并不保证每一次都成功操作。已知：在刚刚打开软件的前几次操作可能不成功，可能卡住，目前原因不明，多试几次就好。~~

- 由于本软件使用 AppleScript，而这个原生语言对于一些软件的窗口没有效用（这些软件不支持 AppleScript 的调度），所以可能在这些软件上 Olive 没发发挥作用。已知：对微信的朋友圈窗口、Telik无法准确调度。
- 对 Finder 多窗口的支持似乎不够好，建议将 Finder 设置为 Tab 显示，FinderFix 这个免费软件可以做到这一点。
- 由于 AppleScript 的特性，本软件只能检测本桌面显示的窗口和所有隐藏的窗口（包括其他桌面），因此会调出其他桌面的隐藏窗口。如果不想在不同的桌面之间不停跳转，可以考虑在 Mission Control 的设置里关闭“When switching to an application, switch to a Space with open windows for the application”
- 只在 Monterey 系统上测试使用了，不知道对 Ventura 的支持如何，未与 Stage Manager 同时测试，估计无法与 Stage Manager 共存。

