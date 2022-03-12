section	.data
	msg		db		'Hello World!', 0Ah
	len		equ		$ - msg

section	.text
	global	_start

_start:
	mov		rax, 1		; invoke SYS_WRITE (kernel opcode 1)
	mov		rdi, 1		; write to the STDOUT file
	mov		rsi, msg	; move the memory address of our message string into ecx
	mov		rdx, len	; number of bytes to write - one for each letter plus 0Ah (line feed character)
	syscall
