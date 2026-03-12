import torch
from IPython import display
from d2l import torch as d2l


def accuracy(y_hat, y):  #将accuracy翻译为“准确数”以便理解
    if len(y_hat.shape) > 1 and y_hat.shape[1] > 1 :
        y_hat = y_hat.argmax(axis=1)
        
    cmp = y_hat.type(y.dtype) == y #bool值张量
    return float(cmp.type(y.dtype).sum()) #即预测对了多少个（True的个数）

def evaluate_accuracy(net, data_iter): #@save

    if isinstance(net, torch.nn.Module):
        net.eval() #设为评估模式，咱也不知道是什么意思

    metric = Accumulator(2)
    with torch.no_grad():
        for X, y in data_iter:
            metric.add(accuracy(net(X), y), y.numel()) #number of elements，shit英语不好还不好理解
            #该行代码表示：metric[0] += accuracy(), metric[1] += y.numel()
        return metric[0] / metric[1]

class Accumulator:  #@save

    def __init__(self, n):
        self.data = [0.0] * n

    def add(self, *args):
        self.data = [a + float(b) for a, b in zip(self.data, args)]
        #就比如说，接收到的args是两个参数，那么这两个参数就会和self.data配对，因为a是self.data里面的，所以就相当于args里和a对应的参数，加到了a对应的位置上

    def reset(self):
        self.data = [0.0] * len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

class Animator:  #动画（造轮子）

    def __init__(self, xlabel=None, ylabel=None, legend=None, xlim=None,
                ylim=None, xscale='linear', yscale='linear', 
                fmts=('-', 'm--', 'g-.', 'r:'), nrows=1, ncols=1,
                figsize=(3.5, 2.5)):

        if legend is None:
            legend =[] #把可能为空的元素或者单元素的东西转换为列表以便访问
        d2l.use_svg_display()
        self.fig, self.axes = d2l.plt.subplots(nrows, ncols, figsize=figsize)
        #窗口， 坐标轴
        if nrows * ncols == 1:
            self.axes = [self.axes, ] #单图时转换为列表，以便于在单图时也能访问

        self.config_axes = lambda: d2l.set_axes(
            self.axes[0], xlabel, ylabel, xlim, ylim, xscale, yscale, legend)
        #便于之后简化代码，定义各参数并建立图表只需要写一遍即可
        self.X, self.Y, self.fmts = None, None, fmts

    def add(self, x, y):
        if not hasattr(y, "__len__"):
            y = [y]
        n = len(y)
        if not hasattr(x, "__len__"):
            x = [x] * n         
        #把x变成和y一样长的列表，点对应。x为一个数时可以理解为在第x天时，每个城市日期相同，但是对应的天气对应的y不同
        if not self.X:
            self.X = [[] for _ in range(n)]
        if not self.Y:
            self.Y = [[] for _ in range(n)]
        
        for i, (a, b) in enumerate(zip(x, y)):
            if a is not None and b is not None:
                self.X[i].append(a)
                self.Y[i].append(b)   
        self.axes[0].cla()   #清除旧图形，这个类的逻辑是加一个点就画一遍图，相当于一帧一帧的搞出来动画
        for x_data, y_data, fmt in zip(self.X, self.Y, self.fmts):
            self.axes[0].plot(x_data, y_data, fmt)  # 逐条绘制曲线
        self.config_axes()
        display.display(self.fig)
        display.clear_output(wait=True)

def train_epoch_ch3(net, train_iter, loss, updater): #@save

    if isinstance(net, torch.nn.Module):
        net.train()

    metric =Accumulator(3)
    for X, y in train_iter:
        y_hat = net(X)
        l = loss(y_hat, y)
        if isinstance(updater, torch.optim.Optimizer):
            updater.zero_grad()
            l.mean().backward()
            updater.step() #根据计算出的梯度更新模型的参数

        else:
            l.sum().backward()
            updater(X.shape[0]) #按照X的0轴长度（即样本数）进行参数更新
        metric.add(float(l.sum()), accuracy(y_hat, y), y.numel())

    return metric[0] / metric[2], metric[1] / metric[2]
    #返回了损失和准确性,注意return不要放在循环里面，不然准确率堪忧

def train_ch3(net, train_iter, test_iter, loss, num_epochs, updater):  #@save
    animator = Animator(xlabel='epoch', xlim=[1,num_epochs], ylim=[0.3, 0.9],
                        legend=['train loss', 'train acc', 'test acc'])

    for epoch in range(num_epochs):
        train_metrics = train_epoch_ch3(net, train_iter, loss, updater)
        test_acc = evaluate_accuracy(net, test_iter)
        animator.add(epoch + 1, train_metrics + (test_acc,))
    train_loss, train_acc = train_metrics #这里的意思应该是，[a, b] + [c, d] = [[a,b], [c,d]]
    assert train_loss < 0.5, train_loss
    assert train_acc <= 1 and train_acc > 0.7, train_acc
    assert test_acc <= 1 and test_acc > 0.7, test_acc
    #assert大概意思是要满足要求才画吧？

def predict_ch3(net, test_iter, n=20):  #@save
    
            for X, y in test_iter:
                break
            trues = d2l.get_fashion_mnist_labels(y)
            preds = d2l.get_fashion_mnist_labels(net(X).argmax(axis=1))
            titles = [true +'\n' + pred for true, pred in zip(trues, preds)]
            d2l.show_images(
                X[0:n].reshape((n, 28, 28)), 2, int(n/2), titles=titles[0:n])