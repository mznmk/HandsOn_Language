%include	'functions.s'

SECTION		.data
	filename	db	'readme.txt',	; the filename to create

SECTION		.text
	global  _start

_start:
	mov		rsi, 0777		; set all permissions to read, write, execute
	mov		rdi, filename	; filename we will create
	mov		rax, 85			; invoke SYS_CREAT (kernel opcode 85)
	syscall

	call	quit			; call our quit function
	