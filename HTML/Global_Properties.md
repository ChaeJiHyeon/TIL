<h1>전역속성</h1>
<ol>
    <li><a href="#Id">id</a></li>
    <li><a href="#Class">class</a></li>
    <li><a href="#Style">style</a></li>
    <li><a href="#Title">title</a></li>
    <li><a href="#Lang">lang</a></li>
    <li><a href="#Data">data</a></li>
    <li><a href="#Draggable">draggable</a></li>
    <li><a href="#Hidden">hidden</a></li>
</ol>
<br />
<br />
<br />
<br />
<h2 id="Id">id</h2>
<p>
    문서 내 고유 식별자, 스타일링할 때 사용<br />
    내용에 공백이 있으면 안된다.<br />
    하나의 아이디만 존재, 시작시 영어소문자<br />
</p>
<br />
<br />
<br />
<br />
<br />
<br />
<h2 id="Class">class</h2>
<p>
    문서 내 식별자, 여러개 가능<br />
    공백으로 여러개 가능 hey ho라고 적으면<br />
    hey클래스와 ho클래스 모두 사용<br />
</p>
<br />
<br />
<br />
<br />
<br />
<br />
<h2 id="Style">style</h2>
<p>
    하나의 요소에만 css스타일 선언<br />
    css파일을 외부에 만들거나 head에 적는 것을 권장한다.<br />
</p>
<br />
<br />
<br />
<br />
<br />
<br />
<h2 id="Title">title</h2>
<p>
    하나의 태그에 툴팁으로 보여준다. <br />
    pre처럼 공백이나 개행을 모두 인정한다. <br />
    툴팁이 상위하위 적용되어 있다면 가장 하위자식의 툴팁이 뜬다. <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
</p>

<h2 id="Lang">lang</h2>
<p>
    언어 태그, head의 charset 컴퓨터가 이해할 수 있는 언어였다면<br />
    lang은 사람이 이해할 수 있는 언어 en이나 ko로 적는다.<br />
    웹접근성(스크린리더)을 높이기 위한 수단이다.<br />
    번역기들이 인지하기 쉽다.<br />
</p>
<br />
<br />
<br />
<br />
<br />
<br />
<h2 id="Data">data</h2>
<p>
    <code>data-속성이름 = &quot;&quot;</code>
    존재하지 않는 속성으로, 사용자가 지정해줄수있다. javascript를 사용할 때,
    <br />
    가지고 이해할 수 있도록 하는 부분이다. <br />
</p>
<br />
<br />
<br />
<br />
<br />
<br />
<h2 id="Draggable">draggable</h2>
<p>
    드래그 기능 여부를 나타내는 열거형 특성 <br />
    true 드래그 할 수 있고 <br />
    false 드래그 못함 <br />
    무조건 true false를 무조건 적어야함. 요소에 따라 다르기 때문에 명시해줘야함.
    <br />
    javascript가 이벤트로 인식할 수 있기 때문에 사용. <br />
</p>
<br />
<br />
<br />
<br />
<br />
<br />
<h2 id="Hidden">hidden</h2>
<p>
    보안상의 정보는 hidden정보를 사용하면 안되고 시각적으로만 보이지 않는
    부분에서만 사용해야한다. <br />
    javascript로 안보이게 설정해야한다. <br />
    css display:flex속성으로 다시 보이게 할 수 있다. <br />
</p>
