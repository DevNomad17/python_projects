from quadratic_eq_plot import SolveQuadratic
from quadratic_eq_plot import SolveSystem
import matplotlib

matplotlib.use('TkAgg')

print('''
 _    _ _       _        _____      _                 _   __  __       _   _     
 | |  | (_)     | |      / ____|    | |               | | |  \/  |     | | | |    
 | |__| |_  __ _| |__   | (___   ___| |__   ___   ___ | | | \  / | __ _| |_| |__  
 |  __  | |/ _` | '_ \   \___ \ / __| '_ \ / _ \ / _ \| | | |\/| |/ _` | __| '_ \ 
 | |  | | | (_| | | | |  ____) | (__| | | | (_) | (_) | | | |  | | (_| | |_| | | |
 |_|  |_|_|\__, |_| |_| |_____/ \___|_| |_|\___/ \___/|_| |_|  |_|\__,_|\__|_| |_|
            __/ |                                                                 
           |___/                                                                  
''')

# For problem statement sq1 see file sq1.png

# sq1 = SolveQuadratic([3, -5, -2])
# sq1.solve()


# For problem statement ss1 see file ss1.png

ss1 = SolveSystem()
ss1.solve()
