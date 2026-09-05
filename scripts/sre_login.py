import requests


class SreLogin:
    def __init__(self):
        self.headers = None
        self.sre_login()

    def sre_login(self):
        sre_url = "https://sre.100credit.cn/api/system/login"
        data = {"username": "chaoyang.yuan", "password": "Minepassword123!"}

        sre_cookie = requests.post(
            sre_url, data=data).cookies.get("sre_cookie_key")
        self.headers = {
            "Content-Type": "application/json",
            "cookie": "sre_cookie_key=" + sre_cookie,
            "x-sre-fingerprint": "eyJ2aXNpdG9ySWQiOiJmMDk4YjFmYWNhZTYyOTJlNWZkMTI5YTNhZGE5MGFkNSIsImNvbXBvbmVudHMiOnsidXNlckFnZW50IjoiIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsInRpbWV6b25lIjoiQXNpYS9TaGFuZ2hhaSIsInNjcmVlblJlc29sdXRpb24iOiIyNTYweDE0NDAiLCJjb2xvckRlcHRoIjoiMzIiLCJwbGF0Zm9ybSI6IldpbjMyIiwiaGFyZHdhcmVDb25jdXJyZW5jeSI6IjIxIn19",
        }

    def sre_get_version(self):
        sre_version_dict = {}
        for project_id in [62, 71, 72]:
            url = f"https://sre.100credit.cn/api/version/page?pageNum=1&pageSize=100&projectId={project_id}"
            resp = (
                requests.get(url, headers=self.headers).json().get(
                    "result").get("list")
            )
            for _ in resp:
                if _.get("status") == 0:
                    sre_version = _.get("jiraVersion")
            if not sre_version:
                sre_version = "暂无可用版本号"
            sre_version_dict[project_id] = sre_version
        print(f"当前 SRE 版本号: {sre_version_dict}")
        return sre_version_dict


SreLogin().sre_get_version()
