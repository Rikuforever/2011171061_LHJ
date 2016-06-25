#Report
by. HoJoong Lee (2011171061)
##Used Datastructure
###Hash
- **개요**  
프로젝트에서 요구하는 기능들중 **검색**이 많은 비중을 차지한다. 예를 들면 특정 user, tweet를 찾아 세부값을 이용하는 경우가 있다. 하지만 user나 tweet의 정보량은 무궁무진하게 커질 수 있기 때문에, 그에 적당한 자료구조로 **Hash** 채택했다. 비록 Hash Table의 메모리 할당량이 클 수 있으나 알맞은 key값을 설정하면 원하는 데이터를 검색하는데 O(1)~O(n)의 빠른 처리를 기대할 수 있다.
- **쓰임**   
	1. **UserDB.list** : User 데이터 묶음  
	주어진 데이터 파일들을 참고해보면 UserProfile의 Identification Number(ID)로 유저를 언급(reference)하는 것을 확인할 수 있다. 그러므로 ID값을 key로 하는 Hash 가 필요함을 느꼈다. 
	2. **TweetDB.list** : Tweet 데이터 묶음  
	기능들중 단어를 검색을 요구하기에 각 글자마다 정수로 변환하여 처리한 특수값을 key로 지정한 Hash를 만들었다. 이때 특수한 경우 다른 단어지만 같은 key값을 공유하는 경우를 방지하고자, Hash Table 접근은 변환한 특수값으로 하되 그 이후 **Linked List**에서의 검색은 단어를 key로 하였다.
###Linked List
