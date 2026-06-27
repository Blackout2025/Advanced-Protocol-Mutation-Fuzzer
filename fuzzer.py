import os
import random
import datetime

# Configuration Variables
CRASH_LOG = "fuzzer_crashes.log"
OUTPUT_HTML = "fuzz_report.html"

# ==========================================================
# 1. THE TARGET PROTOCOL MODEL (UPGRADED BUG MATRIX)
# ==========================================================
def network_service_vulnerability_matrix(packet_bytes):
    """
    Simulates a network parser cluster containing multiple, deep architectural flaws
    including Buffer Overflows, Format String leaks, and Null-Byte disruptions.
    """
    if not packet_bytes.startswith(b"STARK_PROTO"):
        return "ERROR_INVALID_HEADER"

    # BUG DEPLOYMENT 1: Deep Stack Buffer Overflow Limit
    if len(packet_bytes) > 256:
        raise MemoryError("SIGSEGV: Segmentation Fault - Stack Buffer Overflow at 0x7FFFCC23")

    # BUG DEPLOYMENT 2: Format String Flaw Intercept
    if b"%s" in packet_bytes or b"%x" in packet_bytes:
        raise ValueError("SIGILL: Illegal Instruction - Information Leak / CPU Register Pointer Corrupted")

    # BUG DEPLOYMENT 3: Poison Null-Byte Termination Anomaly
    if b"\x00" in packet_bytes and len(packet_bytes) > 50:
        raise OSError("SIGBUS: Bus Error - Null Pointer Dereference Attempted")

    return "SUCCESS_PACKET_PROCESSED"


# ==========================================================
# 2. THE ADVANCED MUTATION toolkit ENGINE
# ==========================================================
def mutate_payload_advanced(iteration):
    """
    Constructs complex, specialized exploit mutations based on classic 
    vulnerability research test patterns.
    """
    base_header = b"STARK_PROTO|"
    
    strategies = [
        # Strategy A: Massive String Padding (Buffer Overflow Hunter)
        lambda: base_header + b"A" * (iteration * 5),
        
        # Strategy B: Format String Pointer Leak Array
        lambda: base_header + b"%s%x%d%n" * random.randint(2, 6),
        
        # Strategy C: Poison Null-Byte Sequence Injector
        lambda: base_header + b"DATA\x00_HIDDEN_PAYLOAD_" + b"B" * 40,
        
        # Strategy D: Clean valid diagnostic pattern
        lambda: base_header + b"CMD_PING_ALIVE"
    ]
    
    return random.choice(strategies)()


# ==========================================================
# 3. CRASH CRUNCHER PIPELINE
# ==========================================================
def execute_campaign(total_iterations=150):
    print("=" * 65)
    print("💥 LAUNCHING ADVANCED SECURITY PROTOCOL MUTATION FUZZER")
    print("=" * 65)
    print("[+] Hunting for memory leaks, pointer corruptions, and overflows...")

    captured_crashes = []
    if os.path.exists(CRASH_LOG):
        os.remove(CRASH_LOG)

    for i in range(1, total_iterations + 1):
        payload = mutate_payload_advanced(i)
        
        try:
            # Deliver mutation payload straight to validation parser
            network_service_vulnerability_matrix(payload)
            
        except (MemoryError, ValueError, OSError) as exploit_exception:
            # INTERCEPT AND TRIAGE THE CRASH LIVE
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_type = type(exploit_exception).__name__
            error_msg = str(exploit_exception)
            
            print(f"[🔥 BUG FOUND] Iteration {i:3d} | Fault: {error_msg.split(' - ')[0]} | Size: {len(payload)} Bytes")
            
            captured_crashes.append({
                "iteration": i,
                "timestamp": timestamp,
                "type": error_type,
                "fault": error_msg,
                "size": len(payload),
                "hex": payload.hex()[:45] + "..."
            })
            
            with open(CRASH_LOG, "a") as log:
                log.write(f"[{timestamp}] {error_type} | {error_msg} | HEX: {payload.hex()}\n")

    generate_advanced_triage_dashboard(total_iterations, captured_crashes)


# ==========================================================
# 4. TRIAGE MANAGEMENT VISUALIZER
# ==========================================================
def generate_advanced_triage_dashboard(total_runs, crashes):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Group distinct types of bugs discovered
    unique_bugs = len(set([c['fault'].split(':')[0] for c in crashes])) if crashes else 0
    
    rows = ""
    for c in crashes:
        color = "#ff7b72" if "SIGSEGV" in c['fault'] else "#f0883e" if "SIGILL" in c['fault'] else "#58a6ff"
        rows += f"""
        <tr style="background-color: #161b22; border-bottom: 1px solid #30363d;">
            <td style="padding:12px; font-family:monospace; color:{color}; font-weight:bold;">{c['fault']}</td>
            <td style="padding:12px; font-family:monospace;">{c['size']} Bytes</td>
            <td style="padding:12px; font-family:monospace; color:#8b949e; font-size:12px;">{c['hex']}</td>
            <td style="padding:12px; text-align:center;">{c['iteration']}</td>
        </tr>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Enterprise Security Vulnerability Triage Matrix</title>
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; background-color: #0d1117; color: #c9d1d9; margin: 40px; }}
        h1 {{ color: #58a6ff; border-bottom: 1px solid #21262d; padding-bottom: 10px; }}
        .grid {{ display: flex; gap: 20px; margin-bottom: 30px; }}
        .card {{ background-color: #161b22; padding: 20px; border-radius: 6px; border: 1px solid #30363d; flex: 1; border-top: 4px solid #30363d; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; border-radius: 6px; overflow: hidden; }}
        th {{ background-color: #21262d; color: #58a6ff; padding: 12px; text-align: left; border-bottom: 1px solid #30363d; }}
    </style>
</head>
<body>
    <h1>💥 Protocol Mutation Fuzzing & Triage Grid</h1>
    <p>Campaign Analysis State Compiled Live: {timestamp}</p>

    <div class="grid">
        <div class="card" style="border-top-color: #58a6ff;">
            <h3>Fuzz Iterations Run</h3>
            <div style="font-size:32px; font-weight:bold; color:#58a6ff;">{total_runs}</div>
        </div>
        <div class="card" style="border-top-color: #ff7b72;">
            <h3>Total System Crashes</h3>
            <div style="font-size:32px; font-weight:bold; color:#ff7b72;">{len(crashes)}</div>
        </div>
        <div class="card" style="border-top-color: #f0883e;">
            <h3>Unique Bugs Triggered</h3>
            <div style="font-size:32px; font-weight:bold; color:#f0883e;">{unique_bugs} Types</div>
        </div>
    </div>

    <h2>🚨 Vulnerability Discovery Stream</h2>
    <table>
        <thead>
            <tr><th>Exception Signature</th><th>Payload Size</th><th>Raw Hex Dump Fingerprint</th><th>Iteration Index</th></tr>
        </thead>
        <tbody>
            {rows if crashes else "<tr><td colspan='4' style='text-align:center; padding:20px; color:#8b949e;'>Campaign complete. Zero exceptions caught.</td></tr>"}
        </tbody>
    </table>
</body>
</html>"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"\n[+] Vulnerability matrix successfully mapped to -> {OUTPUT_HTML}")


if __name__ == "__main__":
    execute_campaign(150)