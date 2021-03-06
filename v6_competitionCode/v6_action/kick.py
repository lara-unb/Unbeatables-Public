# Choregraphe bezier export in Python.
def main(session):
  names = list()
  times = list()
  keys = list()

  names.append("LAnklePitch")
  times.append([1.36, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[0.095066, [3, -0.466667, 0], [3, 0.746667, 0]], [-1.1981, [3, -0.746667, 0], [3, 0.52, 0]], [-1.19349, [3, -0.52, 0], [3, 0.6, 0]], [-1.21497, [3, -0.6, 0], [3, 0.213333, 0]], [-1.19349, [3, -0.213333, 0], [3, 0.44, 0]], [-1.19503, [3, -0.44, 0], [3, 0.866667, 0]], [0.0797259, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("LAnkleRoll")
  times.append([1.36, 2.56, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[-0.113474, [3, -0.466667, 0], [3, 0.4, 0]], [-0.191091, [3, -0.4, 0], [3, 0.346667, 0]], [0.06447, [3, -0.346667, -0.00511331], [3, 0.52, 0.00766996]], [0.07214, [3, -0.52, -0.00213663], [3, 0.6, 0.00246534]], [0.0782759, [3, -0.6, 0], [3, 0.213333, 0]], [0.066004, [3, -0.213333, 0.0083483], [3, 0.44, -0.0172184]], [0.00157595, [3, -0.44, 0.0201455], [3, 0.866667, -0.0396805]], [-0.113474, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("LElbowRoll")
  times.append([1.36, 2.56, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[-0.391128, [3, -0.466667, 0], [3, 0.4, 0]], [-0.329768, [3, -0.4, -0.0147923], [3, 0.346667, 0.01282]], [-0.308291, [3, -0.346667, 0], [3, 0.52, 0]], [-0.31136, [3, -0.52, 0.00306866], [3, 0.6, -0.00354076]], [-0.360448, [3, -0.6, 0], [3, 0.213333, 0]], [-0.322099, [3, -0.213333, -0.00734654], [3, 0.44, 0.0151522]], [-0.292952, [3, -0.44, 0], [3, 0.866667, 0]], [-0.397265, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("LElbowYaw")
  times.append([1.36, 2.56, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[-1.18736, [3, -0.466667, 0], [3, 0.4, 0]], [-1.17815, [3, -0.4, 0], [3, 0.346667, 0]], [-1.1981, [3, -0.346667, 0], [3, 0.52, 0]], [-1.18429, [3, -0.52, 0], [3, 0.6, 0]], [-1.19503, [3, -0.6, 0], [3, 0.213333, 0]], [-1.19349, [3, -0.213333, 0], [3, 0.44, 0]], [-1.19349, [3, -0.44, 0], [3, 0.866667, 0]], [-1.19349, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("LHand")
  times.append([1.36, 2.56, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[0.2936, [3, -0.466667, 0], [3, 0.4, 0]], [0.2856, [3, -0.4, 0.000461546], [3, 0.346667, -0.000400007]], [0.2852, [3, -0.346667, 0], [3, 0.52, 0]], [0.2872, [3, -0.52, 0], [3, 0.6, 0]], [0.2872, [3, -0.6, 0], [3, 0.213333, 0]], [0.282, [3, -0.213333, 0], [3, 0.44, 0]], [0.282, [3, -0.44, 0], [3, 0.866667, 0]], [0.282, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("LHipPitch")
  times.append([1.36, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[0.128898, [3, -0.466667, 0], [3, 0.746667, 0]], [-1.00626, [3, -0.746667, 0.00660725], [3, 0.52, -0.00460148]], [-1.01086, [3, -0.52, 0], [3, 0.6, 0]], [-1.01086, [3, -0.6, 0], [3, 0.213333, 0]], [-1.0078, [3, -0.213333, -0.0030673], [3, 0.44, 0.0063263]], [-0.753151, [3, -0.44, -0.127588], [3, 0.866667, 0.25131]], [0.128898, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("LHipRoll")
  times.append([1.36, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[0.121228, [3, -0.466667, 0], [3, 0.746667, 0]], [0.598302, [3, -0.746667, -0.0132155], [3, 0.52, 0.00920368]], [0.607506, [3, -0.52, -0.00451064], [3, 0.6, 0.00520459]], [0.627448, [3, -0.6, 0], [3, 0.213333, 0]], [0.595234, [3, -0.213333, 0.032214], [3, 0.44, -0.0664414]], [0.0276539, [3, -0.44, 0], [3, 0.866667, 0]], [0.12583, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("LHipYawPitch")
  times.append([1.36, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[-0.170232, [3, -0.466667, 0], [3, 0.746667, 0]], [-0.220854, [3, -0.746667, 0], [3, 0.52, 0]], [-0.21932, [3, -0.52, -0.000949597], [3, 0.6, 0.00109569]], [-0.214718, [3, -0.6, -2.05979e-6], [3, 0.213333, 7.32369e-7]], [-0.214717, [3, -0.213333, 0], [3, 0.44, 0]], [-0.246933, [3, -0.44, 0], [3, 0.866667, 0]], [-0.171766, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("LKneePitch")
  times.append([1.36, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[-0.0951499, [3, -0.466667, 0], [3, 0.746667, 0]], [2.11534, [3, -0.746667, 0], [3, 0.52, 0]], [2.11381, [3, -0.52, 0.000711422], [3, 0.6, -0.000820872]], [2.11074, [3, -0.6, 0], [3, 0.213333, 0]], [2.11534, [3, -0.213333, -0.00116904], [3, 0.44, 0.00241114]], [2.12148, [3, -0.44, 0], [3, 0.866667, 0]], [-0.10282, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("LShoulderPitch")
  times.append([1.36, 2.56, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[1.47873, [3, -0.466667, 0], [3, 0.4, 0]], [1.52015, [3, -0.4, -0.00177029], [3, 0.346667, 0.00153425]], [1.52169, [3, -0.346667, 0], [3, 0.52, 0]], [1.51555, [3, -0.52, 0.00613619], [3, 0.6, -0.00708022]], [1.4818, [3, -0.6, 0], [3, 0.213333, 0]], [1.52475, [3, -0.213333, 0], [3, 0.44, 0]], [1.51708, [3, -0.44, 0.00551], [3, 0.866667, -0.010853]], [1.47567, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("LShoulderRoll")
  times.append([1.36, 2.56, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[0.216252, [3, -0.466667, 0], [3, 0.4, 0]], [0.478566, [3, -0.4, -0.0868354], [3, 0.346667, 0.0752574]], [0.70253, [3, -0.346667, 0], [3, 0.52, 0]], [0.681054, [3, -0.52, 0.00949617], [3, 0.6, -0.0109571]], [0.64117, [3, -0.6, 0], [3, 0.213333, 0]], [0.688724, [3, -0.213333, 0], [3, 0.44, 0]], [0.677985, [3, -0.44, 0.010739], [3, 0.866667, -0.0211526]], [0.216252, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("LWristYaw")
  times.append([1.36, 2.56, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[0.116542, [3, -0.466667, 0], [3, 0.4, 0]], [0.0689882, [3, -0.4, 0.0106832], [3, 0.346667, -0.00925879]], [0.056716, [3, -0.346667, 0], [3, 0.52, 0]], [0.0705221, [3, -0.52, 0], [3, 0.6, 0]], [0.0705221, [3, -0.6, 0], [3, 0.213333, 0]], [0.0674542, [3, -0.213333, 0], [3, 0.44, 0]], [0.0674542, [3, -0.44, 0], [3, 0.866667, 0]], [0.0705221, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("RAnklePitch")
  times.append([1.36, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[0.0874801, [3, -0.466667, 0], [3, 0.746667, 0]], [-0.773094, [3, -0.746667, 0.12335], [3, 0.52, -0.0859045]], [-0.858998, [3, -0.52, 0], [3, 0.6, 0]], [0.748634, [3, -0.6, 0], [3, 0.213333, 0]], [-0.645772, [3, -0.213333, 0.196352], [3, 0.44, -0.404976]], [-1.05535, [3, -0.44, 0], [3, 0.866667, 0]], [0.0828778, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("RAnkleRoll")
  times.append([1.36, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[0.113558, [3, -0.466667, 0], [3, 0.746667, 0]], [-0.061318, [3, -0.746667, 0.00220294], [3, 0.52, -0.00153419]], [-0.0628521, [3, -0.52, 0], [3, 0.6, 0]], [0.122762, [3, -0.6, -0.101093], [3, 0.213333, 0.0359442]], [0.34826, [3, -0.213333, 0], [3, 0.44, 0]], [-0.10427, [3, -0.44, 0], [3, 0.866667, 0]], [0.121228, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("RElbowRoll")
  times.append([1.36, 2.56, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[0.408086, [3, -0.466667, 0], [3, 0.4, 0]], [0.455641, [3, -0.4, -0.018901], [3, 0.346667, 0.0163809]], [0.513931, [3, -0.346667, 0], [3, 0.52, 0]], [0.489388, [3, -0.52, 0], [3, 0.6, 0]], [0.675002, [3, -0.6, 0], [3, 0.213333, 0]], [0.500126, [3, -0.213333, 0.0664525], [3, 0.44, -0.137058]], [0.06447, [3, -0.44, 0], [3, 0.866667, 0]], [0.398881, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("RElbowYaw")
  times.append([1.36, 2.56, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[1.18727, [3, -0.466667, 0], [3, 0.4, 0]], [1.1704, [3, -0.4, 0.00465692], [3, 0.346667, -0.004036]], [1.1612, [3, -0.346667, 0], [3, 0.52, 0]], [1.1704, [3, -0.52, 0], [3, 0.6, 0]], [0.681054, [3, -0.6, 0], [3, 0.213333, 0]], [1.1658, [3, -0.213333, -0.0711275], [3, 0.44, 0.1467]], [1.33454, [3, -0.44, 0], [3, 0.866667, 0]], [1.21642, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("RHand")
  times.append([1.36, 2.56, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[0.2896, [3, -0.466667, 0], [3, 0.4, 0]], [0.2724, [3, -0.4, 0], [3, 0.346667, 0]], [0.2816, [3, -0.346667, -0.000800014], [3, 0.52, 0.00120002]], [0.2828, [3, -0.52, 0], [3, 0.6, 0]], [0.2828, [3, -0.6, 0], [3, 0.213333, 0]], [0.2752, [3, -0.213333, 0], [3, 0.44, 0]], [0.2752, [3, -0.44, 0], [3, 0.866667, 0]], [0.2864, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("RHipPitch")
  times.append([1.36, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[0.128814, [3, -0.466667, 0], [3, 0.746667, 0]], [-0.6704, [3, -0.746667, 0.151984], [3, 0.52, -0.105846]], [-0.776246, [3, -0.52, 0.0712214], [3, 0.6, -0.0821785]], [-1.1306, [3, -0.6, 0], [3, 0.213333, 0]], [-0.589097, [3, -0.213333, 0], [3, 0.44, 0]], [-0.911238, [3, -0.44, 0], [3, 0.866667, 0]], [0.125746, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("RHipRoll")
  times.append([1.36, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[-0.121144, [3, -0.466667, 0], [3, 0.746667, 0]], [0.365133, [3, -0.746667, -0.00220355], [3, 0.52, 0.00153461]], [0.366668, [3, -0.52, 0], [3, 0.6, 0]], [0.362066, [3, -0.6, 0], [3, 0.213333, 0]], [0.366667, [3, -0.213333, 0], [3, 0.44, 0]], [0.135034, [3, -0.44, 0.0549265], [3, 0.866667, -0.108189]], [-0.122678, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("RHipYawPitch")
  times.append([1.36, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[-0.170232, [3, -0.466667, 0], [3, 0.746667, 0]], [-0.220854, [3, -0.746667, 0], [3, 0.52, 0]], [-0.21932, [3, -0.52, -0.000949597], [3, 0.6, 0.00109569]], [-0.214718, [3, -0.6, -2.05979e-6], [3, 0.213333, 7.32369e-7]], [-0.214717, [3, -0.213333, 0], [3, 0.44, 0]], [-0.246933, [3, -0.44, 0], [3, 0.866667, 0]], [-0.171766, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("RKneePitch")
  times.append([1.36, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[-0.091998, [3, -0.466667, 0], [3, 0.746667, 0]], [1.64449, [3, -0.746667, -0.2489], [3, 0.52, 0.173341]], [1.81783, [3, -0.52, 0], [3, 0.6, 0]], [0.43263, [3, -0.6, 0], [3, 0.213333, 0]], [1.38218, [3, -0.213333, -0.183496], [3, 0.44, 0.37846]], [2.1185, [3, -0.44, 0], [3, 0.866667, 0]], [-0.0996681, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("RShoulderPitch")
  times.append([1.36, 2.56, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[1.4374, [3, -0.466667, 0], [3, 0.4, 0]], [1.14441, [3, -0.4, 0.0909441], [3, 0.346667, -0.0788182]], [0.928112, [3, -0.346667, 0], [3, 0.52, 0]], [0.94652, [3, -0.52, 0], [3, 0.6, 0]], [0.84681, [3, -0.6, 0], [3, 0.213333, 0]], [1.05083, [3, -0.213333, -0.0571024], [3, 0.44, 0.117774]], [1.37144, [3, -0.44, -0.0366035], [3, 0.866667, 0.0720979]], [1.44354, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("RShoulderRoll")
  times.append([1.36, 2.56, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[-0.199461, [3, -0.466667, 0], [3, 0.4, 0]], [0.0444441, [3, -0.4, -0.0857396], [3, 0.346667, 0.0743077]], [0.28068, [3, -0.346667, 0], [3, 0.52, 0]], [0.245398, [3, -0.52, 0.00830922], [3, 0.6, -0.00958757]], [0.22699, [3, -0.6, 0], [3, 0.213333, 0]], [0.329768, [3, -0.213333, 0], [3, 0.44, 0]], [-0.665798, [3, -0.44, 0], [3, 0.866667, 0]], [-0.20253, [3, -0.866667, 0], [3, 0, 0]]])

  names.append("RWristYaw")
  times.append([1.36, 2.56, 3.6, 5.16, 5.25, 5.5, 8.92, 11.52])
  keys.append([[0.076658, [3, -0.466667, 0], [3, 0.4, 0]], [0.0536479, [3, -0.4, 0.00931357], [3, 0.346667, -0.00807177]], [0.024502, [3, -0.346667, 0], [3, 0.52, 0]], [0.049046, [3, -0.52, 0], [3, 0.6, 0]], [-0.513932, [3, -0.6, 0], [3, 0.213333, 0]], [0.00916195, [3, -0.213333, -0.108695], [3, 0.44, 0.224183]], [0.484702, [3, -0.44, 0], [3, 0.866667, 0]], [0.128814, [3, -0.866667, 0], [3, 0, 0]]])

  try:
    # uncomment the following line and modify the IP if you use this script outside Choregraphe.
    motion = session.service("ALMotion")
    motion.angleInterpolationBezier(names, times, keys)
  except BaseException, err:
    print err
