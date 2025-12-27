print("Lua Logic Gate: OPEN")

local count = 0
while true do
    -- Simple busy wait simulation
    local start = os.time()
    repeat until os.time() > start + 1
    
    count = count + 1
    print("Lua Calculation Result: " .. (count * 10))
end