import os

# jpg 파일이 있는 디렉토리 경로
directory = 'C:/Users/301-05/Desktop/windows_v1.8.1/data/image'

# 텍스트 파일 경로
output_file = 'C:/Users/301-05/Desktop/train.txt'

# 디렉토리 내의 파일 이름을 가져옵니다.
files = os.listdir(directory)

# jpg 파일 이름들을 담을 리스트 생성
jpg_files = []

# jpg 파일을 필터링하고 파일 이름을 리스트에 추가합니다.
for file in files:
    if file.endswith('.jpg'):
        jpg_files.append('/Desktop/windows_v1.8.1/data/image/' + file)

# 파일 이름들을 텍스트 파일에 씁니다.
with open(output_file, 'w') as f:
    for file_name in jpg_files:
        f.write(file_name + '\n')

print("파일 이름이 성공적으로 저장되었습니다.")