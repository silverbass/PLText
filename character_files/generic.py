import time
commands = {}

@make_cmd
def error(screen, args=[]):
	if screen == 'name':
		return 'error'
	slow_show(screen, ['%s cries pitifully' % name], 0.01)

@make_cmd
def quit(screen, args=[]):
	if screen == 'name':
		return 'quit'
	exit()

@make_cmd
def bind(screen, args=[]):
	if screen == 'name':
		return 'bind'
	if 'to' in args:
		new_cmd, target_cmd = None, None
		new_cmd_arr = args[0:args.index('to')]
		target_cmd_arr = args[args.index('to') + 1::]
		for c in new_cmd_arr:
			if new_cmd == None:
				new_cmd = c
			else:
				new_cmd += ' ' + c
		for c in target_cmd_arr:
			if target_cmd == None:
				target_cmd = c
			else:
				target_cmd += ' ' + c
		if target_cmd in commands:
			make_cmd(commands[target_cmd], new_cmd)
		else:
			slow_show(screen, [target_cmd], 0.01)
	else:
		slow_show(screen, ['No target specified'], 0.01)
