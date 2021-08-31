<h1>시맨틱웹</h1>
<p>
    div로만 구성하면 의미가 없어서 가독성이 떨어지고, 검색엔진이 정보를
    수집하려면 분석에 어려움을 겪어 노출이 어려워지며, 스크린 리더가 읽을 때
    분석이 쉬우니 읽기 쉬워진다. <br /><br />그래서 의미가 있는 semantic웹을 선호하게 된다.<br /><br />
    태그
    <ul>
        <li><a href="#header">header</a></li>
        <li><a href="#nav">nav</a></li>
        <li><a href="#main">main</a></li>
        <li><a href="#article">article</a></li>
        <li><a href="#aside">aside</a></li>
        <li><a href="#footer">footer</a></li>
    </ul>
</p>
<h2 id="header">header</h2>
<p>
    소개 및 탐색, 로고, 검색창, 제목(페이지/글)<br><br>
    한페이지당 하나만 사용하기!<br><br>
    자식 요소로는 다른 header와 footer는 뺀 플로우 컨텐츠
</p>
&nbsp;
&nbsp;
&nbsp;
&nbsp;
<h2 id="nav">nav</h2>
<p>
    현재 페이지의 위치나 다른 페이지의 링크를 넣어준다.
</p>
&nbsp;
&nbsp;
&nbsp;
&nbsp;
<h2 id="aside">aside</h2>
<p>
    추가적 정보지만 없어도 됨.<br><br>
    본문 이해에 필요 있는건 아니여서 광고를 넣을 때도 사용한다.
</p>
&nbsp;
&nbsp;
&nbsp;
&nbsp;
<h2 id="main">main</h2>
<p>
    한번만 사용해야 한다. explorer가 호환이 안된다.
</p>
&nbsp;
&nbsp;
&nbsp;
&nbsp;
<h2 id="article">article</h2>
<p>
    main내 본문에 여러개 가능하다.<br><br>
    독립적으로 구분해서 배포나 재사용이 가능해야 한다.
</p>
&nbsp;
&nbsp;
&nbsp;
&nbsp;
<h2 id="section">section</h2>
<p>
    독립적으로 구분할 수 없어서 section만 가져가면 맥락이 없다.
</p>
&nbsp;
&nbsp;
&nbsp;
&nbsp;
<h2 id="footer">footer</h2>
<p>
    저작권 정보나 관련 문서, 작성자를 적는다.<br><br>
    자식 요소로 hearder나 다른 footer는 사용할 수 없다.
</p>
