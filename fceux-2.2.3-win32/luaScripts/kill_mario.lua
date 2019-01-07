emu.message('ALEX VIEW DID LOAD')

function read_file(file)
	 local input = io.open(file, 'r')

	 if input ~= nil then
	    io.input(input)
	    local content = io.read()
	    io.close(input)
	    os.remove(file)
	    emu.message(content)
	    return content
	 end
	 return nil
end


--memory.writebyte(0x075A, 08)
memory.writebyte(0x07F8, 09)
memory.writebyte(0x07F9, 09)
memory.writebyte(0x07FA, 09)

while true do
      memory.writebyte(0x075A, 08)
      
      value = read_file("../../flask/request.txt")
      if value ~= nil then
      	 if value == "right" then
	    i = 0
	    while i < 10 do
	    	  i = i + 1
	    	  joypad.set(1, {right=1})
		  if i == 5 then
		     joypad.set(1, {A=1})
		  end
		  emu.frameadvance()
	    end
	 elseif value == "left" then
	    start = os.clock()
            while os.clock() - start < 1 do
                  joypad.set(1, {left=1})
                  emu.frameadvance()
            end
	 elseif value == "jump" then
	    start = os.clock()
            while os.clock() - start < 1 do
                  joypad.set(1, {A=1})
                  emu.frameadvance()
            end
	 elseif value == "b" then
	    joypad.set(1, {B=1})
	 end
      end

--memory.writebyte(0x079F, 10)
--memory.writebyte(0x0756, 02)
      emu.frameadvance()
end
--memory.writebyte(0x07F8, 0)
--memory.writebyte(0x07F9, 0)
--memory.writebyte(0x07FA, 0)