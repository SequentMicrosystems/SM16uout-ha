FULL_NAME="Sixteen 0-10V Analog Outputs"
LINK="https://sequentmicrosystems.com/products/sixteen-0-10v-analog-outputs"

import SM16uout
API = SM16uout.SM16uout
DOMAIN = "SM16uout"
NAME_PREFIX = "sm16uo"
SM_MAP = {
    "switch": {
        "led": {
                "chan_no": 16,
                "com": {
                    "get": "get_led",
                    "set": "set_led"
                },
        }
    },
    "number": {
        "out": {
                "chan_no": 16,
                "uom": "V",
                "min_value": 0.0,
                "max_value": 10.0,
                "step": 0.01,
                "com": {
                    "get": "get_u_out",
                    "set": "set_u_out"
                },
                "icon": {
                    "on": "mdi:flash-triangle",
                    "off": "mdi:flash-triangle"
                }
        },
    },
}
