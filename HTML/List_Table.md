<h1>목록과 표</h1>
<ol>
    <li><a href="#List">목록</a><ul>
        <li>&lt;ul&gt;</li>
        <li>&lt;ol&gt;</li>
        <li>&lt;dl&gt;</li>
    </ul></li>
    <li><a href="#Table">표</a></li>
</ol>
<br />
<br />
<br />
<br />
<h2 id="#List">목록</h2>
<p>
    ul과 ol태그는 li를 자식 요소로 사용하며 서로 중첩이 가능하다.<br>
</p>
<p>
    <ul>
        <li>&lt;ul&gt;</li><br>
        <p>이렇게 순서 없이 나타나는 태그는 unordered list태그이다.</p><br>
        <ol>
            <li type="1">&lt;ol&gt;</liㅍ미ㅕ>
            <p>이렇게 순서가 있는 경우에는 ordered list 태그를 사용한다.</p>
            <li>type속성</li>
            <p>알파벳 순으로 나타내고 싶은 경우에는 a, A 로마숫자순은 i, I, default값은 1이다.</p>
            <li value="5">start속성</li>
            <p>중간에 시작 수를 바꾸고 싶은 경우 쓰는 속성으로 숫자를 값으로 넣는다.<br>
            이와 같은 속성으로 <code>&lt;li&gt;</code>태그에 <code>value</code>속성을 이용하면 된다.</p>
            <li>reversed속성</li>
            <p>true와 false값을 갖는데 true값을 가지면 역순으로 나온다.</p>
        </ol>
    </ul>
    <br>
    <br>
    <dl>
        <dt><code>&lt;dt&gt;</code>term, 용어</dt>
        <dd><code>&lt;dd&gt;</code>description, 설명을 넣으면 된다.</dd>
        <dd>용어와 설명은 일대일,일대다,다대일의 관계가 모두 가능하고 <code>div</code>로 감싸서 스타일링을 한다.</dd>
        <dd>dt와 dd의 형제는 서로만 가능하다.</dd>
    </dl>
</p>
<br />
<br />
<br />
<br />
<br />
<br />
<h2 id="#Table">표</h2>
<p>
    <ul>
        <li>caption</li><br>
        <p>테이블의 제목, table태그의 첫번째 자식, thead의 앞에 있어야 한다.</p><br><br>
        <li>tr</li><br>
        <p>table row, 표의 열(줄)로 줄마다 넣는다.</p><br><br>
        <li>th<ul><li>속성:scope</li><p>col, row를 사용하며 어디의 기준인지일 때 사용한다.</p></ul></li><br>
        <p>table head로 표의 제목을 넣는 부분이다.
        </p><br><br>
        <li>td<ul><li>속성:colspan</li><p>숫자를 값으로 적으며 차지하는 칸을 적을 수 있다.</p></ul></li><br>
        <p>table data, 제목의 값을 넣는다.</p><br><br>
        <li>thead</li><br>
        <p>구획을 나누어 접근성을 높일 때 사용한다. table의 바로 아래 적어야한다.</p><br><br>
        <li>tbody</li><br>
        <p>구획을 나눌때 사용하는 부분이다.</p><br><br>
        <li>tfoot</li><br>
        <p>구획을 나누어 총 갯수를 표현할 때 사용하는 부분이다.</p><br><br>
    </ul>
</p>
