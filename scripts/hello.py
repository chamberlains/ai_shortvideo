import sys
import os
import requests


class SreLogin:
    def __init__(self):
        self.headers = None
        self.sre_login()

    def sre_login(self):
        sre_url = "https://sre.100credit.cn/api/system/login"
        data = {"username": "chaoyang.yuan", "password": "Minepassword123!"}

        print("🔑 正在尝试登录 SRE 系统...")
        resp = requests.post(sre_url, data=data)
        sre_cookie = resp.cookies.get("sre_cookie_key")

        if not sre_cookie:
            print(f"⚠️ 登录可能失败，未能获取到 sre_cookie_key。响应内容: {resp.text[:200]}")
            sre_cookie = ""

        self.headers = {
            "Content-Type": "application/json",
            "cookie": "sre_cookie_key=" + str(sre_cookie),
            "x-sre-fingerprint": "eyJ2aXNpdG9ySWQiOiJmMDk4YjFmYWNhZTYyOTJlNWZkMTI5YTNhZGE5MGFkNSIsImNvbXBvbmVudHMiOnsidXNlckFnZW50IjoiIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsInRpbWV6b25lIjoiQXNpYS9TaGFuZ2hhaSIsInNjcmVlblJlc29sdXRpb24iOiIyNTYweDE0NDAiLCJjb2xvckRlcHRoIjoiMzIiLCJwbGF0Zm9ybSI6IldpbjMyIiwiaGFyZHdhcmVDb25jdXJyZW5jeSI6IjIxIn19",
        }

    def sre_get_version(self):
        sre_version_dict = {}
        for project_id in [62, 71, 72]:
            url = f"https://sre.100credit.cn/api/version/page?pageNum=1&pageSize=100&projectId={project_id}"
            sre_version = None  # 提前初始化变量，防止未定义报错

            try:
                res_json = requests.get(
                    url, headers=self.headers, timeout=10).json()
                resp = res_json.get("result", {}).get(
                    "list", []) if res_json.get("result") else []

                for item in resp:
                    if item.get("status") == 0:
                        sre_version = item.get("jiraVersion")
            except Exception as e:
                print(f"❌ 获取项目 {project_id} 版本失败: {e}")

            if not sre_version:
                sre_version = "暂无可用版本号"
            sre_version_dict[project_id] = sre_version

        print("========================================")
        print(f"🎉 当前 SRE 版本号: {sre_version_dict}")
        print("========================================")
        return sre_version_dict


if __name__ == "__main__":
    SreLogin().sre_get_version()
