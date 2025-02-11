import wzero as wz

dataset = wz.datasets.Mnist().distrib_thermometer(10).flatten()
model = wz.models.WiSARD2(7840, 40, 10)
data = wz.experiments2.profile(dataset, model)

print(data)
