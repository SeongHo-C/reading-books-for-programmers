<!--
bold 처리
** **

js 코드 작성
```js

```

링크
[보여질 단어](URL 주소)

형광펜 처리
` `

글자색
<span style="color:red"> </span>
-->

## Chapter 14: 가상 메모리

<details>
<summary>Table of Contents</summary>

- 연속 메모리 할당[:link:](#연속-메모리-할당)
  - 스와핑[:link:](#스와핑)
  - 메모리 할당[:link:](#메모리-할당)
  - 외부 단편화[:link:](#외부-단편화)
- 페이징을 통한 가상 메모리 관리[:link:](#페이징을-통한-가상-메모리-관리)
  - 페이징이란[:link:](#페이징이란)
  - 페이지 테이블[:link:](#페이지-테이블)
  - 페이징에서의 주소 변환[:link:](#페이징에서의-주소-변환)
  - 페이지 테이블 엔트리[:link:](#페이지-테이블-엔트리)
  </details>

### 연속 메모리 할당

프로세스에 연속적인 메모리 공간을 할당하는 방식을 `연속 메모리 할당` 방식이라고 한다.

#### 스와핑

입출력 작업의 요구로 대기 상태가 된, 오랫동안 사용되지 않은 프로세스들을 임시로 보조기억장치 일부 영역으로 쫓아내고, 그렇게 해서 생긴 메모리상의 빈 공간에 또 다른 프로세스를 적재하여 실행하는 방식을 `스와핑`이라고 한다.

- 프로세스들이 쫓겨나는 보조기억장치의 일부 영역을 `스왑 영역`
- 현재 실행되지 않는 프로세스가 메모리에서 스왑 영역으로 옮겨지는 것을 `스왑 아웃`
- 스왑 영역에 있던 프로세스가 다시 메모리로 옮겨오는 것을 `스왑 인`

스와핑을 이용하면 프로세스들이 요구하는 메모리 주소 공간의 크기가 실제 메모리 크기보다 큰 경우에도 프로세스들을 동시 실행할 수 있다.

#### 메모리 할당

비어 있는 메모리 공간에 프로세스를 연속적으로 할당하는 방식에는 대표적으로 `최초 적합`, `최적 적합`, `최악 적합`의 세 가지 방식이 있다.

`최초 적합`

- 운영체제가 메모리 내의 빈 공간을 순서대로 검색하다가 적재할 수 있는 공간을 발견하면 그 공간에 프로세스를 배치하는 방식이다.
- 최초 적합 방식은 프로세스가 적재될 수 있는 공간을 발견하는 즉시 메모리를 할당하는 방식이므로 검색을 최소화할 수 있고 결과적으로 빠른 할당이 가능하다.

`최적 적합`

- 운영체제가 빈 공간을 모두 검색해 본 후, 프로세스가 적재될 수 있는 공간 중 가장 작은 공간에 프로세스를 배치하는 방식이다.

`최악 적합`

- 운영체제가 빈 공간을 모두 검색해 본 후, 프로세스가 적재될 수 있는 공간 중 가장 큰 공간에 프로세스를 배치하는 방식이다.

#### 외부 단편화

메모리 할당

<img width="500" alt="image" src="https://github.com/SeongHo-C/reading-books-for-programmers/assets/83394485/b3a87056-01ab-4df4-9b5e-0347b54d977c">

메모리 해제

<img width="500" alt="image" src="https://github.com/SeongHo-C/reading-books-for-programmers/assets/83394485/84f6beb8-736f-4f57-93ad-69992e2b99d0">

프로세스를 메모리에 연속적으로 배치하는 연속 메모리 할당은 메모리를 효율적으로 사용하는 방법이 아니다. 왜냐하면 연속 메모리 할당은 `외부 단편화`라는 문제를 내포하고 있기 때문이다.

프로세스들이 메모리에 연속적으로 할당되는 환경에서는 위와 같이 프로세스들이 실행되고 종료되기를 반복하며 메모리 사이 사이에 빈 공간들이 생긴다. 프로세스 바깥에 생기는 이러한 빈 공간들은 분명 빈 공간이지만 그 공간보다 큰 프로세스를 적재하기 어려운 상황을 초래하고, 결국 메모리 낭비로 이어진다. 이러한 현상을 `외부 단편화`라고 한다.

외부 단편화를 해결할 수 있는 대표적인 방안으로 메모리를 `압축`하는 방법이 있다. 압축은 여기저기 흩어져 있는 빈 공간들을 하나로 모으는 방식으로 메모리 내에 저장된 프로세스를 적당히 재배치시켜 여기저기 흩어져 있는 작은 빈 공간들을 하나의 큰 빈 공간으로 만드는 방법이다.

압축 방식의 단점 </br>
⓵ 작은 빈 공간들을 하나로 모으는 동안 시스템은 하던 일을 중지 </br>
⓶ 메모리에 있는 내용을 옮기는 작업은 많은 오버헤드를 야기 </br>
⓷ 어떤 프로세스를 어떻게 움직여야 오버헤드를 최소화하며 압축할 수 있는지에 대한 명확한 방법을 결정하기 어려움

### 페이징을 통한 가상 메모리 관리

프로세스를 메모리에 연속적으로 할당하는 방식은 두 가지 문제를 내포하고 있다. 한 가지는 외부 단편화이고, 또 하나는 물리 메모리보다 큰 프로세스를 실행할 수 없다는점이다.

`가상 메모리`는 실행하고자 하는 프로그램을 일부만 메모리에 적재하여 실제 물리 메모리 크기보다 더 큰 프로세스를 실행할 수 있게 하는 기술이다. 이를 가능케 하는 가상 메모리 관리 기법에는 크게 `페이징`과 `세그멘테이션`이 있다.

#### 페이징이란

연속 메모리 할당 방식에서 외부 단편화가 생긴 근본적인 이유는 각기 다른 크기의 프로세스가 메모리에 연속적으로 할당되었기 때문이다.

페이징은 프로세스의 논리 주소 공간을 `페이지`라는 일정한 단위로 자르고, 메모리 물리 주소 공간을 `프레임`이라는 페이지와 동일한 크기의 일정한 단위로 자른 뒤 페이지를 프레임에 할당하는 가상 메모리 관리 기법이다.

페이징에서도 스와핑을 사용할 수 있다. 메모리에 적재될 필요가 없는 페이지들은 보조기억장치로 스왑 아웃되고, 실행에 필요한 페이지들은 메모리로 스왑 인된다. 페이징 시스템에서의 스왑 아웃은 `페이지 아웃`, 스왑 인은 `페이지 인`이라고 부르기도 한다.

즉, 프로세스를 이루는 페이지 중 실행에 필요한 일부 페이지만을 메모리에 적재하고 당장 실행에 필요하지 않은 페이지들은 보조기억장치에 남겨둘 수 있다.

#### 페이지 테이블

🚨 프로세스가 메모리에 불연속적으로 배치되면 CPU 입장에서 '다음에 실행할 명령어 위치'를 찾기가 어려워진다.

이를 해결하기 위해 페이징 시스템은 프로세스가 비록 (실제 메모리 내의 주소인) 물리 주소에 불연속적으로 배치되더라도 (CPU가 바라보는 주소인) 논리 주소에는 연속적으로 배치되도록 `페이지 테이블`을 이용한다.

- 페이지 테이블은 페이지 번호와 프레임 번호를 짝지어 주는 일종의 이정표이다.
- CPU로 하여금 페이지 번호만 보고 해당 페이지가 적재된 프레임을 찾을 수 있게 한다.

페이징은 외부 단편화 문제를 해결할 수 있지만, `내부 단편화`라는 문제를 야기할 수 있다. 가령 페이지 크기가 10KB인데, 프로세스의 크기가 108KB라고 한다면 마지막 페이지는 2KB만큼의 크기가 남는다. 이러한 메모리 낭비를 내부 단편화라고 한다. 그렇기에 내부 단편화를 적당히 방지하면서 너무 크지 않은 페이지 테이블이 만들어지도록 페이지의 크기를 조정하는 것이 중요하다.

프로세스마다 각자의 프로세스 테이블을 가지고 있고 각 프로세스의 페이지 테이블들은 메모리에 적재되어 있다. 그리고 CPU 내의 `페이지 테이블 베이스 레지스터(PTBR)`는 각 프로세스의 페이지 테이블이 적재된 주소를 가리키고 있다.

🚨 그런데 이렇게 페이지 테이블을 메모리에 두면 메모리 접근 시간이 두 배로 늘어난다. 메모리에 있는 페이지 테이블을 보기 위해 한 번, 그렇게 알게 된 프레임에 접근하기 위해 한 번, 이렇게 총 두 번의 메모리 접근이 필요하기 때문이다.

이와 같은 문제를 해결하기 위해 CPU 곁에 (일반적으로 MMU 내에) `TLB(Translation Lookaside Buffer)`라는 페이지 테이블의 캐시 메모리를 둔다. TLB는 페이지 테이블의 캐시이기 때문에 페이지 테이블의 일부 내용을 저장한다. 참조 지역성에 근거해 주로 최근에 사용된 페이지 위주로 가져와 저장한다.

- CPU가 발생한 논리 주소에 대한 페이지 번호가 TLB에 있을 경우 이를 `TLB 히트`라고 한다.
- 페이지 번호가 TLB에 없을 경우 어쩔 수 없이 페이지가 적재된 프레임을 알기 위해 메모리 내의 페이지 테이블에 접근할 수 밖에 없다. 이를 `TLB 미스`라고 한다.

#### 페이징에서의 주소 변환

하나의 페이지 혹은 프레임은 여러 주소를 포괄하고 있다. 그렇기에 특정 주소를 접근하려면 아래와 같은 두 가지 정보가 필요하다.

- 어떤 페이지 혹은 프레임에 접근하고 싶은지
- 접근하려는 주소가 그 페이지 혹은 프레임으로부터 얼마나 떨어져 있는지

페이징 시스템에서는 모든 논리 주소가 기본적으로 `페이지 번호`와 `변위`로 이루어져 있다.
페이지 테이블에서 해당 페이지 번호를 찾으면 페이지가 어떤 프레임에 할당되었는지를 알 수 있다. 변위는 접근하려는 주소가 프레임의 시작 번지로부터 얼만큼 떨어져 있는지를 알기 위한 정보이다.

즉, 논리 주소 <페이지 번호, 변위>는 페이지 테이블을 통해 물리 주소 <프레임 번호, 변위>로 변환된다.

#### 페이지 테이블 엔트리

페이지 테이블의 각 엔트리, 다시 말해 페이지 테이블의 각각의 행들을 `페이지 테이블 엔트리(PTE)`라고 한다. 페이지 테이블 엔트리에는 페이지 번호, 프레임 번호 이외에도 다른 중요한 정보들이 있다. 대표적인 것이 유효 비트, 보호 비트, 참조 비트, 수정 비트이다.

`유효 비트`

현재 해당 페이지에 접근 가능한지 여부를 알려준다.

현재 페이지가 메모리에 적재되어 있는지 아니면 보조기억장치에 있는지를 알려주는 비트이다. 즉, 페이지가 메모리에 적재되어 있다면 유효 비트가 1, 페이지가 메모리에 적재되어 있지 않다면 유효 비트가 0이 된다.

만일 CPU가 유효 비트가 0인 메모리에 적재되어 있지 않은 페이지로 접근하려고 하면 어떻게 될까❓ </br>
이 경우 `페이지 폴트`라는 예외(Exception)가 발생한다.

CPU가 페이지 폴트를 처리하는 과정은 하드웨어 인터럽트를 처리하는 과정과 유사하다. </br>
⓵ CPU는 기존의 작업 내역을 백업한다. </br>
⓶ 페이지 폴트 처리 루틴을 실행한다. </br>
⓷ 페이지 처리 루틴은 원하는 페이지를 메모리로 가져온 뒤 유효 비트를 1로 변경해 준다. </br>
⓸ 페이지 폴트를 처리했다면 이제 CPU는 해당 페이지에 접근할 수 있게 된다.

`보호 비트`

페이지 보호 기능을 위해 존재하는 비트이다.

보호 비트를 통해 해당 페이지가 읽고 쓰기가 모두 가능한 페이지인지, 혹은 읽기만 가능한 페이지인지를 나타낼 수 있다. 가령 비트가 0일 경우 이 페이지는 읽기만 가능한 페이지임을 나타내고, 1일 경우 읽고 쓰기가 모두 가능한 페이지이다.

보호 비트는 세 개의 비트로 조금 더 복잡하게 구현할 수도 있다. 읽기(Read)를 나타내는 r, 쓰기(Write)를 나타내는 w, 실행(eXecute)을 나타내는 x의 조합으로 읽기, 쓰기, 실행하기 권한의 조합을 나타낼 수 있다.

`참조 비트`

CPU가 이 페이지에 접근한 적이 있는지 여부를 나타낸다.

적재 이후 CPU가 읽거나 쓴 페이지는 참조 비트가 1로 세팅되고, 적재 이후 한 번도 읽거나 쓴 적이 없는 페이지는 0으로 유지된다.

`수정 비트`

해당 페이지에 데이터를 쓴 적이 있는지 없는지 수정 여부를 알려준다. `더티 비트`라고도 부른다.

이 비트가 1이면 변경된 적이 있는 페이지, 0이면 변경된 적이 없는 페이지(한 번도 접근한적 없거나 읽기만 했던 페이지)임을 나타낸다.

수정 비트는 왜 존재하는 것일까❓</br>
수정 비트는 페이지가 메모리에서 사라질 때 보조기억장치에 쓰기 작업을 해야 하는지, 할 필요가 없는지를 판단하기 위해 존재한다.
