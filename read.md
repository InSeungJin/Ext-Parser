1. 현재까지 제작 분기
{
    시작, main화면
            |
    확장자에 따른 옵션 리스트 출력
            |
    ext관련 중요 정보 출력(1/2)
            |
            ?
}

2. 개선점
{
    1. 옵션 파싱부분 변경하기 (os모듈에서 os.path)
    2. GUI 환경구성 (tkinter 사용)(필수 아님) -> 필요하다면 나중에 별도로 제작
    3. 반복되는 부분 함수화
}

3. 추후 추가할것
{
    1. inode를 이용한 파일(디렉터리)개수 출력 및 inode에 대한 더 자세한 정보 출력
    2. ext4까지의 호환성을 위해 inode에 대한 size및 기타 차이점에대해 ext3이전과 다른형식으로 파싱
}