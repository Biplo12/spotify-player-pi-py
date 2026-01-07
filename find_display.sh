#!/bin/bash

echo "Finding the active display..."
echo ""

# Method 1: Check who's logged in
echo "Method 1: Check logged in users with displays:"
who | grep '(:' || echo "  No users logged into graphical session"

echo ""

# Method 2: Check X sockets
echo "Method 2: Available X displays:"
ls -la /tmp/.X11-unix/ 2>/dev/null | grep "^s" | awk '{print $9}' | sed 's/X/:/' || echo "  No X sockets found"

echo ""

# Method 3: Check active display processes
echo "Method 3: Active display processes:"
ps aux | grep -E "[X]org|[X]server" | head -3 || echo "  No X server processes found"

echo ""

# Method 4: Test displays
echo "Method 4: Testing displays:"
for disp in :0 :1 :10; do
    DISPLAY=$disp xset q >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "  ✓ Display $disp is active"
        # Try to get the logged-in user for this display
        export DISPLAY=$disp
        USER=$(who | grep "($disp)" | awk '{print $1}' | head -n1)
        if [ -n "$USER" ]; then
            echo "    Logged in user: $USER"
        fi
    else
        echo "  ✗ Display $disp is not accessible"
    fi
done

echo ""
echo "Recommended display:"
# Try to find the best display
if DISPLAY=:0 xset q >/dev/null 2>&1; then
    echo "  Use: export DISPLAY=:0"
elif DISPLAY=:1 xset q >/dev/null 2>&1; then
    echo "  Use: export DISPLAY=:1"
else
    echo "  Could not detect active display"
    echo "  You may need to log in to the desktop first"
fi
