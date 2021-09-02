<h1>임베디드 요소</h1>
<p>외부 소스를 불러와서 삽입한다.<br>이미지, 오디오 등 멀티미디어 요소들이 해당된다.</p>
<ol>
    <li><a href="#Image">img</a><ul>
        <li>&lt;src&gt;</li>
        <li>&lt;alt&gt;</li>
        <li>&lt;title&gt;</li>
        <li>&lt;width, height&gt;</li>
        <li>&lt;srcset&gt;</li>
        <li>&lt;sizes&gt;</li>
    </ul></li>
    <li><a href="#Video">video</a></li>
    <li><a href="#Audio">audio</a></li>
    <li><a href="#Canvas">canvas</a></li>
    <li><a href="#Iframe">iframe</a></li>
</ol>
<br />
<br />
<br />
<br />
<h2 id="#Image">img</h2>
<p>
    이미지 요소<br>
</p>
<ol>
    <li>src</li>
    <p>필수 경로(source), 절대 경로나 상대 경로를 넣으면 된다.</p>
    <li>srcset</li>
    <p><code>이미지파일명 공백 너비서술자(w)(작은걸 먼저 넣는다)/픽셀밀도서술자(x)</code></p>
    <li>sizes</li>
    <p>미디어 조건문들을 정의<code>(max-width:480px) 480px,</code> 이런 식으로 적는다.</p>
    <li>alt</li>
    <p>이미지의 텍스트 설명, 깨진 형태 이미지일 경우 대체가 가능하다.</p>
    <li>title</li>
    <p>이미지 위에 두면 설명(툴팁)이 뜬다.</p>
    <li>width, height</li>
    <p>숫자를 적을 수 있다, 하나를 지정하면 지정된 부분에 맞춰 비율 그대로 변화한다.</p>
</ol>
<br>
<br>
<p>이미지 유형<br> <b>[래스터, 확대시키면 깨진다]</b>JPEG, PNG, GIF, WEBP, <br><b>[벡터, 확대시 깨지지 않는다.]</b>SVG</p>
<br />
<br />
<br />
<br />
<br />
<br />
<h2 id="#Video">video</h2>
<p>video를 표시하는 요소, 닫는 태그가 존재</p>
<p>
    <ul>
        <li>src</li>
        <p>필수 경로(source), 절대 경로나 상대 경로를 넣으면 된다.</p>
        <li>autoplay</li>
        <p>boolean속성으로 이 값이 설정되면 로딩이 완료되지 않더라도 자동 재생된다.</p>
        <li>controls</li>
        <p>소리조절, 일시정지 재시작을 할 수 있는 컨트롤러를 제공한다.</p>
        <li>loop</li>
        <p>boolean속성으로 재생이 마친 후 자동으로 처음으로 돌아간다.</p>
        <li>poster</li>
        <p>출력되는 포스터이다.</p>
        <li>width, height</li>
        <p>숫자를 적을 수 있다, 하나를 지정하면 지정된 부분에 맞춰 비율 그대로 변화한다.</p>
    </ul>
</p>
<br />
<br />
<br />
<br />
<br />
<br />
<h2 id="#Audio">audio</h2>
<p>audio를 표시하는 요소, MP3, WAV, Ogg형식을 공식적으로 지원한다.</p>
<p>
    <ul>
        <li>src</li>
        <p>필수 경로(source), 절대 경로나 상대 경로를 넣으면 된다.</p>
        <li>controls</li>
        <p>소리조절, 일시정지 재시작을 할 수 있는 컨트롤러를 제공한다.</p>
        <li>autoplay</li>
        <p>오디오 자동 재생 여부</p>
        <li>loop</li>
        <p>오디오 반복 재생 여부</p>
    </ul>
</p>
<br />
<br />
<br />
<br />
<br />
<br />
<h2 id="#Audio">canvas</h2>
<p>그래픽과 애니메이션을 그릴 수 있다. 대화형 콘텐츠가 아닌 요소를 말한다.<br>
닫는 태그를 필요로 한다. CSS로 크기를 바꾸는 것보다 HTML내 속성으로 크기를 바꾸는 것이 좋다.</p>
<p>
    <ul>
        <li>height</li>
        <p>기본값은 150px이다.</p>
        <li>width</li>
        <p>기본값은 300px이다.</p>
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
