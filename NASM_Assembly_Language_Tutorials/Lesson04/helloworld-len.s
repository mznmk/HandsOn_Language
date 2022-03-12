section		.data
	msg		db		'Hello, brave new world!', 0Ah

section		.text
	global	_start

_start:
	mov		rax, msg
	call	strlen

	mov		rdx, rax		; our function leaves the result in RAX
	mov		rsi, msg		; this is all the same as before
	mov		rdi, 1
	mov		rax, 1
	syscall

	mov		rax, 60
	mov		rdi, 0
	syscall

strlen:						; this is our first function declaration
	push	rbx				; push the value in RBX onto the stack to preserve it while we use RBX in this function
	mov		rbx, rax		; move the address in RAX into RBX (Both point to the same segment in memory)

nextchar:					; this is the same as lesson3
	cmp		byte [rax], 0
	jz		finished
	inc		rax
	jmp		nextchar

finished:
	sub		rax, rbx		; pop the value on the stack back into RBX
	pop		rbx				; return to where the function was called
	ret
