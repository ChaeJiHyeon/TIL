<h1>메타데이터 요소</h1>
<a href="#meta">meta</a><br />
<a href="#title">title</a><br />
<a href="#mime">MIME type</a><br />
<a href="#st">style</a><br />
<a href="#scr">script</a><br />
<br />
<br />
<br />
<br />
<h2 id="#meta">meta</h2>
<p>
    빈요소이다. 그래서 속성을 사용한다.<br><br>
    name속성과 content 속성을 같이 적는다.(키와 값이라고 생각하면 된다.)<br><br>
    여러 개 사용이 가능하다.<br><br>
    <ul>
        <li>application(name속성에 적기)</li><br><br>
        <p>하나만 가능하다. title과의 차이점은 title은 페이지 이동시 변화할 수 있지만 application name은 네이버 같은 느낌이다.</p><br><br>
        <li>description(name속성에 적기)</li><br><br>
        <p>설명과 즐겨찾기</p><br><br>
        <li>generator(name속성에 적기)</li><br><br>
        <p>페이지 생성</p><br><br>
        <li>keywords(name속성에 적기)</li><br><br>
        <p>해쉬태그로 이해하면 된다. 쉼표로 여러가지 적을 수 있음.</p><br><br>
        <li>referrer(name속성에 적기)</li><br><br>
        <p>HTTP에서 흔적을 남기는 헤더</p><br><br>
        <li>charset(name속성에 적기)</li><br><br>
        <p>문자 인코딩, 여러 언어를 지원하는 UTF-8<br>
        head태그의 첫번째 또는 title태그를 적기 전에 적어야 함</p><br><br>
        <li>viewport(name속성에 적기)</li><br><br>
        <p>뷰포트, 모바일 장치에서 사용하기 위해 사용한다.</p><br><br>
        <ul>
            <li>width, height(content에 적기)</li><br><br>
            <p>device-width, 하나만 지정해도 알아서 바뀐다.</p><br><br>
            <li>initial-scale(content에 적기)</li><br><br>
            <p>1.0이 기본</p><br><br>
            <li>user-scalable(content에 적기)</li><br><br>
            <p>확대속성, 기본 값 yes</p><br><br>
        </ul>
    </ul>
</p>
<br />
<br />
<br />
<br />
<h2 id="#title">title</h2>
<p>
    탭 제목 부분, head태그 내에 딱 하나 존재한다!<br /><br /><br />
    잘 작성해야지 검색 엔진이 광고라고 생각하지 않는다.<br /><br />
    단순한 단어 나열은 광고라고 인식한다.<br /><br />
</p>
<br />
<br />
<br />
<br />
<h2 id="#mime">MIME Type</h2>
<p>
    외부 경로를 불러올 때 어떤 파일인지 해석하게 하기 위해 타입을 명시한다.<br /><br />
    <code>type = text/css</code> 대분류/확장자 순이며 소문자로 명시하는걸 권고한다.<br /><br />
</p>
<br />
<br />
<br />
<br />
<h2 id="#st">style</h2>
<p>
    스타일 정보 요소로 css부분 <br /><br />
    외부에서 링크로 가져오는 걸 권장, 중복될 경우 아래있는 것이 사용됨<br /><br />
</p>
<br />
<br />
<br />
<br />
<h2 id="#scr">script</h2>
<p>
    JavaScript부분을 적음, src 속성으로 경로를 연결할 수 있다. <br />
    head에도 body에도 둘 다 있어도 된다.<br /><br />
    script가 나오면 script를 먼저 해석하기 때문에 시간이 걸려서 body의 마지막 부분에 적는걸 추천한다.<br /><br />
</p>
