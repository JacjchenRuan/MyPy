###莫烦pytorch###

# #激活函数
import torch
import torch.nn.functional as F
from torch.autograd import Variable
import matplotlib.pyplot as plt
x = torch.linspace(-5,5,200)#-5-5,200个点
# x = Variable(x)#将x变成变量形式
x_np = x.data.numpy()
y_relu = F.relu(x).data.numpy()
y_sigmoid = F.sigmoid(x).data.numpy()
y_tanh = F.tanh(x).data.numpy()
y_softplus = F.softplus(x).data.numpy()
plt.figure(1,figsize=(8,6))
plt.subplot(221)
plt.plot(x_np,y_relu,label='relu')
plt.subplot(222)
plt.plot(x_np,y_sigmoid,label='sigmoid')
plt.subplot(223)
plt.plot(x_np,y_tanh,label='tanh')
plt.subplot(224)
plt.plot(x_np,y_softplus,label='softplus')
plt.show()

# #拟合回归
# import torch
# from torch.autograd import Variable
# import torch.nn.functional as F
# import matplotlib.pyplot as plt
# x = torch.unsqueeze(torch.linspace(-1,1,100),dim=1)#将以为数据转化成二维
# y = x.pow(2) + 0.2 * torch.rand(x.size())
# class Net(torch.nn.Module):
#     def __init__(self,n_input,n_hidden,n_output):#设置神经元的个数（输入层，隐藏层，输出层）
#         super(Net,self).__init__()#类的继承
#         self.hidden = torch.nn.Linear(n_input,n_hidden)#形成神经元之间的连线
#         self.output = torch.nn.Linear(n_hidden,n_output)
#     def forward(self,x):#此处的x为input
#         x = F.relu(self.hidden(x))#此处的x为将输入层的数据转化为隐藏层
#         x = self.output(x)#此处的x为将隐藏层的数据变成最终所要的结果。因为这里处理的是回归问题，最终所得为具体数值，所以输出是不用激励函数
#         return x
# net = Net(1,10,1)
# print(net)
#
# plt.ion()#实时打印
# plt.show()
# #开始进行优化
# optimizer = torch.optim.SGD(net.parameters(),lr=0.5)#传入神经网络参数用SGD随机梯度下降法优化，lr为学习率
# loss_fun = torch.nn.MSELoss()#MSELoss均方差来处理回归问题
# for t in range(100):#训练100步
#     prediction = net(x)
#     loss = loss_fun(prediction,y)#用损失函数计算误差
#     optimizer.zero_grad()#梯度初始化为0
#     loss.backward()#自动反向传递
#     optimizer.step()#以学习率0.5，进行梯度优化
#     if t % 5 == 0:#每五步打印一次
#         plt.cla()#清除轴，当前活动轴在当前图中。 它保持其他轴不变。
#         plt.scatter(x.data.numpy(),y.data.numpy())
#         plt.plot(x.data.numpy(),prediction.data.numpy(),color='red')
#         plt.text(0.5,0,'Loss=%.4f'%loss.item())
#         plt.pause(0.1)
# plt.ioff()
# plt.show()

#分类问题