import re

def initDictCounter():
	slovar = {};
	count = 0;
	filePath = input("Enter result file: ");
	file = open(filePath, 'r');
	for line in file:
		bytesTuple = re.findall(r'\d+', line);
		slovar.update({(bytesTuple[0], bytesTuple[1]): bytesTuple[2]});
		count += int(bytesTuple[2]);
	file.close();
	return (slovar, count);

def splitString():
	strings = [];
	filePath = input("Enter file to check: ");
	l = input("Enter l: ");
	file = open(filePath, 'rb');
	string = file.read();
	for index in range(0,len(string)):
		strings.append(string[index:index + int(l)]);
	file.close;
	return strings;

def p1(x0, table, count):
    count_x0=0;
    for i in range(0, 256):
        count_x0 += int(table[tuple([str(x0), str(i)])]);
    return count_x0 / count;

def p2(x0,x1, table, count):
    count_x0=0;
    for i in range(0, 256):
        count_x0 += int(table[tuple([str(x0),str(i)])]);
    return int(table[tuple([str(x0), str(i)])]) / count_x0;

def calculations(table, count, strings):
	opt = [];
	result = 1;
	for string in strings:
		for i in range(len(string)):
			if i == 0:
				result *= p1(string[i], table, count);
			else:
				result *= p2(string[i-1],strings[i], table, count);
		opt.append(result);
		result = 1;
	return opt;

def main():
	resultHex = "";
	resultChar = "";
	slovar = initDictCounter();
	table = slovar[0];
	count = slovar[1];
	strings = splitString();
	opt = calculations(table, count, strings);
	estimate = min(opt);
	resultBytes = strings[opt.index(estimate)];
	print("The upper estimate: " + str(estimate));
	temp = list(resultBytes)
	for i in range(len(temp)):
		if temp[i] != 0:
			resultChar += chr(temp[i]);
		else:
			resultChar += ".";
	print("String: " + resultChar);
	print("Hex: " + resultBytes.hex());


if __name__ == "__main__":
	main()