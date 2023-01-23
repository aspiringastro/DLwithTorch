import torch


x = torch.rand(2,5)
x_one = torch.ones(size=x.size(), dtype=x.dtype)
y = torch.rand(5,2)
y_one = torch.ones(size=y.size(), dtype=y.dtype)
print(x, y)

z = x @ y
print(z)

print(
    x.shape, y.shape, z.shape, x_one.shape, y_one.shape
)

print(x + x_one, y + y_one, x * x_one, y * y_one)