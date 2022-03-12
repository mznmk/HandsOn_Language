%include	'functions.s'

SECTION		.data
	filename	db	'readme.txt', 0h		; the filename to create
	contents	db	'Hello world!', 0h		; the contents to write

SECTION		.text
	global  _start

_start:
	mov		rsi, 0777		; Create file from lesson 22
	mov		rdi, filename
	mov		rax, 85
	syscall

	mov		rdx, 12			; Write contents to file from lesson 23
	mov		rsi, contents
	mov		rdi, rax
	mov		rax, 1
	syscall

	mov		rsi, 0			; flag for readonly access mode (O_RDONLY)
	mov		rdi, filename	; filename we created above
	mov		rax, 2			; invoke SYS_OPEN (kernel opcode 2)
	syscall

	call	iprintLF		; call our integer printing function

	call	quit			; call our quit function
	