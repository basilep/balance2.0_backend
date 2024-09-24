
def decode_alarme_from_decimal(decimal_data):
    binary_data = f'{int(decimal_data):014b}'
    alarmes = []
    if binary_data [13] == '1':
        alarmes.append(1)
    if binary_data [12] == '1':
        alarmes.append(2)
    if binary_data [11] == '1':
        alarmes.append(3)
    if binary_data [10] == '1':
        alarmes.append(4)
    if binary_data [9] == '1':
        alarmes.append(5)
    if binary_data [8] == '1':
        alarmes.append(6)
    if binary_data [7] == '1':
        alarmes.append(7)
    if binary_data [6] == '1':
        alarmes.append(8)
    if binary_data [5] == '1':
        alarmes.append(9)
    if binary_data [4] == '1':
        alarmes.append(10)
    if binary_data [3] == '1':
        alarmes.append(11)
    if binary_data [2] == '1':
        alarmes.append(12)
    if binary_data [1] == '1':
        alarmes.append(13)
    if binary_data [0] == '1':
        alarmes.append(14)
    return alarmes