spinlock = 363
circular_buffer = [0]
position = 0
last = 2017
for i in range(last):
    position = ((position + spinlock) % len(circular_buffer)) + 1
    circular_buffer.insert(position, i + 1)
short_circuit = circular_buffer[circular_buffer.index(last) + 1]
print("answer 1:", short_circuit)

spinlock = 363
position = 0
for i in range(50000000):
    position = ((position + spinlock) % (i + 1)) + 1
    if position == 1:
        short_circuit = i + 1
print("answer 2:", short_circuit)
