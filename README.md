#启动命令：
不生成html报告：hrun testcases/login.yml  
生成html报告：hrun testcases/login.yml --html=path/name.html  
生成allure报告：hrun testcases/login.yml --alluredir=path/allure_report  
***
#启动查看allure报告
需安装allure，并配置环境变量  
cmd中输入命令：allure server path/allure_report
***
#解决log中报句柄无效
httprunner库中打开runner.py，在test_start下增加代码  
```
 log_handler = logger.add(self.__log_path, level="DEBUG")
 
 # 句柄错误解决方法
        def setup_ansi_colors(suppress_colors):
            convert_ansi_codes_to_win32_calls = False
            if os.name == 'nt':
                # Only need to init colorama with 'convert=True' when app is called
                # from 'cmd.exe', 'powershell' or 'git-bash via VS Code'
                convert_ansi_codes_to_win32_calls = 'TERM' not in os.environ or \
                                                    os.environ.get('TERM_PROGRAM', None) == 'vscode'
            if 'CONVERT_ANSI_CODES_TO_WIN32_CALLS' in os.environ:
                # explicit option is useful for cases when automatic guess fails (e.g. for Eclipse IDE)
                convert_ansi_codes_to_win32_calls = os.environ.get('CONVERT_ANSI_CODES_TO_WIN32_CALLS').lower() in (
                    'true', '1')
            colorama.init(strip=suppress_colors, convert=convert_ansi_codes_to_win32_calls)
            
        setup_ansi_colors(suppress_colors=False)
        logger.remove()
        log_handler = logger.add(sink=sys.stdout.write,colorize=True)
