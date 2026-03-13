# ClaudeFigma

Claude Code에서 Figma MCP를 사용하는 프로젝트입니다.

## Figma MCP 설정

### 1. Figma Personal Access Token 발급

1. [Figma](https://www.figma.com) 로그인
2. 우측 상단 프로필 > **Settings**
3. **Security** 탭 > **Personal access tokens** > **Generate new token**
4. 토큰 이름 입력 후 생성 및 복사

### 2. 환경변수 설정

```bash
export FIGMA_API_KEY="your_figma_personal_access_token"
```

영구 설정을 원하면 `~/.bashrc` 또는 `~/.zshrc`에 추가하세요.

### 3. MCP 서버 실행 확인

Claude Code를 이 프로젝트 디렉토리에서 실행하면 `.mcp.json` 설정에 따라
Figma MCP 서버가 자동으로 시작됩니다.

## 사용 가능한 기능

- Figma 파일 및 컴포넌트 조회
- 디자인 토큰 추출
- 레이아웃 및 스타일 정보 읽기
- 컴포넌트 구조 분석
