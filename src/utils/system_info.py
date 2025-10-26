"""System information utilities"""
import platform
import psutil
import os

class SystemInfo:
    def __init__(self):
        self.platform = platform.system()
        self.platform_release = platform.release()
        self.platform_version = platform.version()
        self.architecture = platform.machine()
        self.processor = platform.processor()
        self.ram_gb = round(psutil.virtual_memory().total / (1024**3), 2)
        self.cpu_cores = os.cpu_count()
        self.is_android = self._detect_android()
        self.is_termux = self._detect_termux()
    
    def _detect_android(self) -> bool:
        """Detect if running on Android"""
        return os.path.exists('/system/build.prop') or 'ANDROID_ROOT' in os.environ
    
    def _detect_termux(self) -> bool:
        """Detect if running in Termux"""
        return os.path.exists('/data/data/com.termux') or 'TERMUX_VERSION' in os.environ
    
    def __str__(self):
        return f"{self.platform} {self.architecture} | {self.ram_gb}GB RAM | {self.cpu_cores} cores"
