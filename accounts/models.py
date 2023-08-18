from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.db import models


# UserManager의 create_user를 오버라이딩 해서 사용
class UserManager(BaseUserManager):
    def create_user(self, username, password, nickname, staff=False, admin=False, active=True):
        # username, password, nickname을 필드로 가지는 UserManager상속
        if not username:
            raise ValueError("id를 입력해주세요")
            # username가 (None, 빈 문자열 등)을 확인합니다,만약 username가 비어있을때에 예외를 발생시키고, id를 입력해주세요 라는 메시지 전달
        if not password:
            raise ValueError("pw를 입력해주세요")
            # password가 (None, 빈 문자열 등)을 확인하고,만약 password가 비어있을때에 예외를 발생시키고, pw를 입력해주세요 라는 메시지 전달
        if not nickname:
            raise ValueError("닉네임을 입력해주세요")
            # (None, 빈 문자열 등)을 확인하고,만약 nickname가 비어있을때에 예외를 발생시키고, 닉네임을 입력하세요 라는 메시지 전달
            # if문 -> 유효성 검사

        self.user = self.model(username=username, nickname=nickname)
        # user객체를 생성하는 코드

        self.user.set_password(password)
        # user객체의 set_password

        self.user.staff = staff
        # 사용자가 관리자 측면(staff)에서 접근할 수 있는지 여부를 나타냄

        self.user.admin = admin
        # admin 권한을 가지고 있는 지 여부를 나타냄

        self.user.active = active
        # active 값은 사용자 계정이 활성화 상태인지 여부를 나타냄

        self.user.save(using=self._db)
        # 데이터베이스에 새로운 레코드를 생성하는 작업을 수행

        return self.user

    def create_superuser(self, username, password, nickname):
        # UserManager 클래서에서 슈퍼유저를 생성

        user = self.create_user(
            # create_user메서드를 호출하여 새로운 객체를 생성
            # staff, admin을 True를 주면서 슈퍼유저를 생성
            username,
            password,
            nickname,
            staff=True,
            admin=True,
        )

        return user
        # 생성된 user를 return해준다.


class User(AbstractBaseUser):
    username = models.CharField(max_length=150, primary_key=True, verbose_name="사용자 아이디")
    # 문자열을 가진 데이터를 저장, 최대 길이 150, 기본키 설정

    password = models.CharField(max_length=20, blank=False, verbose_name="비밀번호")
    # 문자열을 가진 데이터를 저장, 문자열 최대길이 20, 공백을 가질수 없다.

    nickname = models.CharField(
        max_length=20, null=False, blank=False, verbose_name="닉네임"
    )
    # 문자열을 가진 데이터를 저장, 문자열 최대길이 20, null가질수 없다, 공백을 가질수 없다.

    active = models.BooleanField(default=True)
    # 사용자의 활성화 상태를 표시하는 필드
    staff = models.BooleanField(default=False)
    # 유저를 생성할때 관리자 대시보드에 접근할 권한이 없게 설정

    admin = models.BooleanField(default=False)
    # 관리자를 생성할것인지 판별하는것, 관리자계정을 생성할때에 False값으로 설정

    # Post관련 필드
    # post_number = models.AutoField(default=0, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    # USERNAME_FIELD 속성은 사용자 이름으로 사용할 필드를 지정합니다. 여기에서는 username를 사용자 이름으로 설정

    REQUIRED_FIELDS = ['nickname']
    # 사용자 객체를 생성할 때 필수로 입력해야하는 필드

    objects = UserManager()
    # UserManager 클래스의 인스턴스를 생성하고 이를 objects 속성에 할당

    def __str__(self):
        return self.username
    # 이 메서드는 객체를 문자열로 변환했을 때 표시되는 값을 정의합니다. self.username를 통해 해당 객체의 username를 반환하도록 설정

    def is_staff(self):
        return self.staff
    # 사용자의 staff 속성 값을 반환하므로, 사용자가 스태프 권한을 가지면 True를 반환하고, 그렇지 않으면 False를 반환

    def is_superuser(self):
        return self.admin
    # 이 메서드는 사용자가 최고 관리자(admin) 인지 확인

    def has_perm(self, perm, obj=None):
        return self.admin
    # 이 메서드는 사용자가 주어진 권한(perm)을 가지고 있는지 확인

    def has_module_perms(self, app_label):
        return self.admin
    # 이 메서드는 사용자가 주어진 앱(app_label)에 대한 권한을 가지고 있는지 확인합니다.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post_number = models.AutoField(primary_key=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Post: {self.title}"
