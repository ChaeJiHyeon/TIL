<h1>HTML의 구조, 빈 요소, 요소의 중첩, 주석</h1>
<a href="#Structure">HTML의 구조</a><br />
<a href="#Empty">빈 요소</a><br />
<a href="#Nesting">요소의 중첩</a><br />
<a href="#Comment">주석</a><br />
<br />
<br />
<br />
<br />
<h2 id="#Structure">HTML의 구조</h2>
<p>
    <b
        ><code>< ></code> Opening Tag와 내용 그리고 <code>< / ></code> Closing
        Tag</b
    >로 존재하며 이는 한 요소라고 할 수 있다.<br />
    <br /><br />
    Opening Tag와 Closing Tag는 보이지 않고 내용만 보이게 되며<br /><br />
    이러한 내용을 적을 때 호환성을 위해 HTML5 웹 표준에 맞게 적는다.<br /><br />
    그 중 하나는 태그의 이름은 <b>소문자</b>로 적어야 한다는 것이다.<br /><br />
    <br /><br /><br /><br /><br /><br />
    <code>DOCTYPE</code>부분은 문서 타입을 적는 부분이다.<br /><br />
    현재 html5가 표준화가 되어 html이라고 적으면 되지만 예전에는 브라우저가
    코드를 해당 html버전에 맞는 문법으로 해석하기 위해 사용했었다.<br /><br /><br />
    <code>html</code>부분은 하나만 존재하며, 전체 컨텐츠를 감싸는 루트 요소로
    사용된다.<br /><br /><br />
    <code>head</code>부분 또한 하나만 존재하며, html에 포함된다. <br /><br />
    <b>화면에 보이지 않는 웹 브라우저가 식별할 수 있는 페이지의 정보</b>를 적는
    부분이다.<br /><br />
    브라우저 모두 지원하는 요소이며 tab에 뜨는 title을 적거나 meta tag 즉,
    인코딩 정보나 문서 정보(meta data)를 적는다.<br /><br /><br />
    <code>body</code>부분은 <b>화면에 보이는 부분</b>으로 HTML문서의 내용이다.
    이 태그는 html의 두번째 자식 요소로 포함된다.<br /><br />
    <p style="font-size: 0.5em">(HTML의 문서 구조는 basic파일에 적혀 있다.)</p>
</p>
<br />
<br />
<br />
<br />
<h2 id="Empty">빈 요소</h2>
<p>
    내용(Text, element)을 갖지 않아도 되는 태그를 말한다.<br />
    <br /><br />
    <code> br, hr, img, meta, input</code>
    등이 존재한다. <br /><br />
    보시다시피 Opening Tag는 필요하지만 Closing Tag는 필요하지 않다.<br /><br />
    html5에서 <code> br / </code> 또는 <code>br</code>은 선택이지만 일관성 있게
    적는 것이 다른 사람과 코드를 공유할 때 좋다.<br /><br /><br />
    주의할 점은 Opening Tag와 Closing Tag 사이 내용이 없다고 빈 태그가 되는 것이
    아니라는 점이다.
</p>
<br />
<br />
<br />
<br />
<h2 id="Nesting">요소의 중첩</h2>
<p>
    요소 안에 다른 요소가 들어가는 포함관계를 가진 경우를 말한다.
    <br /><br />
    <code>ul</code>태그와 <code>li</code>태그를 예시로 볼 수 있다.<br /><br />
    <code>ul</code>태그 안에 <code>li</code>태그가 들어가기 때문에
    <code>ul</code>태그를 부모 요소, 상위 요소라고 하며 <code>li</code>태그를
    자식 요소, 하위 요소라고 한다.<br /><br />
    이러한 중첩관계는 들여쓰기를 통해 구분한다.
</p>
<br />
<br />
<br />
<br />
<h2 id="Comment">주석</h2>
<p>
    브라우저가 무시하는 태그로 코드에 메모하거나 임시 코드를 처리하는 용으로
    사용된다.<br />
    <br /><br />
    <code> < ! - - 내용 - - ></code>
    로 적는다. <br /><br />
</p>
