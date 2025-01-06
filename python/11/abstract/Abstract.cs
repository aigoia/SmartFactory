using System;

abstract class Unit
{
    public abstract float HpPower();
    public abstract float MpPower();
}

class Player : Unit
{
    private float hp;
    private float mp;

    public Player(float hp, float mp)
    {
        this.hp = hp;
        this.hp = mp;
    }

    public override float HpPower()
    {
        return this.hp ** this.hp;
    }

    public override float MpPower()
    {
        return this.mp ** this.mp;
    }
}

// 추상클래스는 클래스의 메타 클래스이다
// 보통 팀원들에게 코드 구조를 강제하기 위해 사용한다
// 합을 맞춘 사이라면 추상 클래스가 구지 필요 없지만 그런 경우는 드물다