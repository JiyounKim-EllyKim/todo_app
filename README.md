# todo_app

# repository 만들 때 처음부터 파일이 존재하게 만들면(ex. README.md 또는 License 등)
# Sourcetree 사용 시 고려할 사항
## 1. clone으로 시작하기(원격지에 있는 파일부터 시작해서 로컬 레포지토리에 프로젝트 시작하면 OK)
## 2. 그런데 이미 로컬 레포지토리에 이미 파일이 존재하면 Sourcetree로 pull부터 시작해도 브랜치가 나뉘어 있다.
      (2번과 같은 경우에는 git bash로 git cli환경에서 명령어로 처리해야 한다.)

```bash
# 로컬 레포지토리에서
git init

git remote add origin <원격지 주소>

git pull origin main

git add -A

git commit -m'<커밋 메시지>'

git push origin main
```
