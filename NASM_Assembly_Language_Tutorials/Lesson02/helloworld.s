section		.data
	msg		db		'Hello World!', 0Ah
	len		equ		$ - msg

section		.text
	global	_start

_start:
	mov		rax, 1
	mov		rdi, 1
	mov		rsi, msg
	mov		rdx, len
	syscall

	mov		rax, 60		; invoke SYS_EXIT (kernel opcode 60)
	mov		rdi, 0		; return 0 status on exit - 'No Errors'
	syscall
