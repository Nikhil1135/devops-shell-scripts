# 📅 Day 5 - Linux System Monitoring with Bash 🧠

## 📌 Objective

To monitor key system metrics — **CPU**, **Memory**, and **Disk** — using shell scripting, with log-based output and real-time parsing using Unix commands.

---

## ✅ Topics Covered

- Shell script automation for monitoring
- Real-time resource usage via:
  - `top`, `free -m`, `df -h`
- Parsing outputs using `awk`, `grep`
- Understanding CPU idle vs usage
- Calculating memory consumption
- Logging results with timestamps
- Concepts like: `NR==2`, `\$2 + \$4`, `printf`, `$(...)`

---

## 🛠️ Files

| File | Description |
|------|-------------|
| `sys_monitor.sh` | Main script that logs CPU, Memory, and Disk usage to a file |

---

## 📂 Script Output

Each time the script runs, it generates a log file:

```bash
sys_health_YYYY-MM-DD.log


========================================OUTPUTS===================================================================
[2025-07-07 17:21:44] ========== System health check started ==========
[2025-07-07 17:21:44] The CPU usage is: 12.5%
[2025-07-07 17:21:44] The Memory usage is: Used: 328MB / Total: 949MB
[2025-07-07 17:21:44] The Disk usage on / is: 64%
[2025-07-07 17:21:44] ========== System health check finished ==========
==================================================================================================================


Commands Practiced
Command	Purpose
top -bn1	---------------Get snapshot of CPU usage
grep "Cpu(s)" -----------Filter only CPU data
awk '{print $2 + $4}'	---Add user + system CPU usage
free -m	-----------------Get memory usage in MB
df -h /	-----------------Get disk usage for root (/) partition
awk 'NR==2{...}'	-------Process only second line of output
printf	-----------------Format output cleanly
watch -n 3 free -m	-----Monitor memory every 3 seconds (live)
=========================================================================================================
Key Learnings
NR==2 → used to select the second row from command output (usually where data lives)

$2, $3, $4 → positional columns from command output (e.g., total, used, free)

$(...) → Command substitution to assign output to variables

Used functions in bash (log()) to handle timestamped logging

Simple logging format for clear auditing
