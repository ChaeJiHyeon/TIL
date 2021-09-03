<h1>Form태그</h1>
<p>
    정보를 입력해 줄 수 있는 장치<br>
    단독으로 사용하면 아무것도 보이지 않고, 그 안에 텍스트와 버튼을 넣어줘야 보인다.<br>
    대화형 컨트롤이 들어가는 부분으로 인라인 요소이다.
</p>

<ol>
    <li><a href="#Label">&lt;label&gt;</a>
        <ul>
            <li>for</li>
            <li>name</li>
        </ul>
    </li>
    <li><a href="#Input">input</a>
        <ul>
            <li>type</li>
            <li>name</li>
            <li>placeholder</li>
            <li>autocomplete</li>
            <li>required</li>
            <li>disabled</li>
            <li>readonly</li>
            <li>step</li>
            <li>min</li>
            <li>max</li>
        </ul>
    </li>
    <li><a href="#Fieldset">fieldset</a></li>
    <li><a href="#Button">button</a>
        <ul>
            <li>type</li>
        </ul>
    </li>
    <li><a href="#Select">select</a>
        <ul>
            <li>required</li>
            <li>&lt;option&gt;</li>
            <li>&lt;optgroup&gt;</li>
        </ul>
    </li>
    <li><a href="#Datalist">datalist</a>
        <ul>
            <li>select</li>
            <li>&lt;option&gt;</li>
        </ul>
    </li>
    <li><a href="#Textarea">textarea</a>
        <ul>
            <li>rows</li>
            <li>cols</li>
            <li>disable</li>
            <li>required</li>
            <li>placeholder</li>
        </ul>
    </li>
</ol>
<br />
<br />
<br />
<br />
<h2 id="#Label">label</h2>
<p>
    form의 자식요소(input과 select)의 제목<br>
</p>
<div>
<code>
    &lt;form&nbsp;action="GET"&gt;
</code>
</div>
<div>
    
<code>
    &nbsp;&nbsp;&nbsp;&nbsp;&lt;label for=&quot;test&quot;&gt;Test : &lt;/label&gt;<br>
</code>
</div>
<div>
<code>
    &nbsp;&nbsp;&nbsp;&nbsp;&lt;input type=&quot;text&quot; id=&quot;test&quot;&gt;<br>
</code>
</div>
<div>
<code>
    &lt;/form&gt;
</code>
</div>
<br />
<br />
<ol>
    <li>for</li>
    <p>자식요소의 id값을 가지며 필수다, 하지만 label의 자식요소로 input이 들어가는 경우에는 for를 안넣어도 된다.</p>
    <li>name</li>
    <p>서버로 전송하는 값의 이름</p>
</ol>
<br>
<br>
<br />
<br />
<br />
<br />
<h2 id="#Input">input</h2>
<p>
    label과 함께 적는다, 적으면 접근성에 좋다.<br>
    div로 묶어주면 div가 블록요소여서 알아서 개행이 된다.<br>
</p>
<p>
    <ul>
        <li>type   
            <pre>text(한줄만, enter를 치면 submit됨) - minlength="", maxlength="" 갯수가 작을경우 툴팁보여줌
            password(안보이게 해줌(마스킹).post로 보내야함!)
            email(형식에 맞지않으면 에러메시지를 툴팁으로 보여줌)
            tel(형식과 관계없이 보내지긴 함)
            number(숫자입력, 숫자가 아니면 에러메시지를 툴팁으로 보여줌)
            range(범위를 고를 수 있는 위젯, )
            date(날짜, 시간 제외, 년월일)
            month(년월)
            week(주)
            time(시간)
            submit(기본값이 제출/submit) - 문구 변경시 value="적으면된다."
            button(동작을 하지 않는다.) - 문구 변경시 value="적는다."
            reset(기본값초기화, form내부가 초기값으로 변경됨) - value=""
            checkbox(체크, 중복선택, checked 불린 속성-> 자동으로 true로 들어감)
            radio(name을 갖게 해야지 선택되는 항목이 하나.)- value로 구분
            file(파일 제출)</pre>
        </li>
        <li>name
            <p>
                서버에 전송할 때 사용
            </p>
        </li>
        <li>placeholder
            <p>
                힌트
            </p>
        </li>
        <li>autocomplete
            <p>
                자동완성(on-이전값이 보인다. off-이전값이 안보인다.)
            </p>
        </li>
        <li>required
            <p>
                불린 속성, 필수(질문)적으로 요구된다.
            </p>
        </li>
        <li>disabled
            <p>
                불린속성, 입력도 안되고 제출도 안되는 비활성화 상태
            </p>
        </li>
        <li>readonly
            <p>
                불린 속성, 값을 value로 미리 지정하고 수정할 수 없다.
            </p>
        </li>
        <li>step
            <p>
                시작단계 기준으로 지정수만큼 올라가고 줄어든다
                </p>
        </li>
        <li>min, max
            <p>
                숫자 범위, 유효성 검사 해줌
            </p>
        </li>
        <li>max</li>
    </ul>
</p>
<br />
<br />
<br />
<br />
<br />
<br />
<h2 id="#Fieldset">fieldset</h2>
<p>설문조사 폼에 input이 많은 경우<br>
    개인정보, 부가정보, 주소연락처를 넣는 회원가입폼<br>
    그룹으로 나눠서 시맨틱적 측면을 챙기고 싶다면 fieldset사용<br>
    legend태그(범례, 부모가 무조건 fieldset이여야 함.)로 제목을 적을 수 있다.</p>
<br />
<br />
<br />
<br />
<br />
<br />
<h2 id="#Button">button</h2>
<p>
    <ul>
        <li>type</li>
        <p>submit, reset, button(기본값)<br>
        빈요소가 아님, 내용을 적지 않으면 텍스트가 안들어감.</p>
    </ul>
</p>
<br />
<br />
<br />
<br />
<br />
<br />
<h2 id="#Iframe">iframe</h2>
<p>다른 HTML페이지를 삽입할 때 사용한다.</p>
<p>
    <ul>
        <li>height, width</li>
        <li>src</li>
        <p>경로 지정</p>
    </ul>
</p>
