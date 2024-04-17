# The original automata list

automata = [
    {
        "id": "1",
        "alphabet": ["a"],
        "states": ["0"],
        "initial_states": ["0"],
        "final_states": ["0"],
        "transitions": []
    },
    {
        "id": "2",
        "alphabet": ["a"],
        "states": ["0"],
        "initial_states": ["0"],
        "final_states": ["0"],
        "transitions": [
            "0a0"
        ]
    },
    {
        "id": "3",
        "alphabet": ["a"],
        "states": ["0", "1"],
        "initial_states": ["0"],
        "final_states": ["1"],
        "transitions": [
            "0a1"
        ]
    },
    {
        "id": "4",
        "alphabet": ["a"],
        "states": ["0", "1"],
        "initial_states": ["0"],
        "final_states": [],
        "transitions": [
            "0a1"
        ]
    },
    {
        "id": "5",
        "alphabet": ["a", "b"],
        "states": ["1", "2", "3", "4"],
        "initial_states": ["1", "3"],
        "final_states": ["2", "4"],
        "transitions": [
            "1a2",
            "1b0",
            "3a0",
            "3b4",
            "0a0",
            "0b0"
        ]
    },
    {
        "id": "6",
        "alphabet": ["a", "b"],
        "states": ["0", "1", "2", "3"],
        "initial_states": ["1", "3"],
        "final_states": ["2", "0"],
        "transitions": [
            "1a2",
            "3b0"
        ]
    },
    {
        "id": "7",
        "alphabet": ["a"],
        "states": ["0", "1"],
        "initial_states": ["1"],
        "final_states": ["0"],
        "transitions": [
            "1a0",
            "1a1"
        ]
    },
    {
        "id": "8",
        "alphabet": ["a"],
        "states": ["1", "0"],
        "initial_states": ["1"],
        "final_states": ["0"],
        "transitions": [
            "1a0",
            "0a0"
        ]
    },
    {
        "id": "9",
        "alphabet": ["a", "b"],
        "states": ["0", "1", "2", "3", "4", "5"],
        "initial_states": ["1"],
        "final_states": ["0"],
        "transitions": [
            "1a2",
            "2a3",
            "2b3",
            "3a4",
            "4a5",
            "4b5",
            "5a0"
        ]
    },
    {
        "id": "10",
        "alphabet": ["a", "b"],
        "states": ["0", "1", "2", "3", "4"],
        "initial_states": ["0"],
        "final_states": ["0"],
        "transitions": [
            "0a1",
            "2a3",
            "3a4",
            "4a0"
        ]
    },
    {
        "id": "11",
        "alphabet": ["a", "b"],
        "states": ["0", "1", "2", "3", "4", "5"],
        "initial_states": ["0"],
        "final_states": ["2"],
        "transitions": [
            "0b3",
            "0a2",
            "1a3",
            "1b3",
            "2a1",
            "2b0",
            "3a3",
            "3b3"
        ]
    },
    {
        "id": "12",
        "alphabet": ["a", "b", "c", "d"],
        "states": ["0", "1"],
        "initial_states": ["1"],
        "final_states": ["1"],
        "transitions": [
            "1a2",
            "1c0",
            "0b0",
            "0d1"
        ]
    },
    {
        "id": "13",
        "alphabet": ["a"],
        "states": ["0", "1", "2", "3", "4", "5", "6", "7"],
        "initial_states": ["1"],
        "final_states": ["3", "4", "5", "6", "7", "0"],
        "transitions": [
            "1a2",
            "2a3",
            "3a4",
            "4a5",
            "5a6",
            "6a7",
            "7a0",
            "0a0"
        ]
    },
    {
        "id": "14",
        "alphabet": ["a", "b", "c", "d"],
        "states": ["0", "1", "2", "3"],
        "initial_states": ["0"],
        "final_states": ["1"],
        "transitions": [
            "0a0",
            "0b2",
            "2b2",
            "2c3",
            "3c3",
            "3d1",
            "1d1",
            "0c3",
            "0d1",
            "2d1"
        ]
    },
    {
        "id": "15",
        "alphabet": ["a", "b", "c", "d"],
        "states": ["0", "1", "2", "3", "4"],
        "initial_states": ["1"],
        "final_states": ["4"],
        "transitions": [
            "0a0",
            "1a1",
            "1b2",
            "1c3",
            "1d4",
            "2b2",
            "2c3",
            "2d4",
            "3c3",
            "3d4",
            "3a0",
            "3b0",
            "4d4",
            "4a4",
            "4b4",
            "4c4"
        ]
    },
    {
        "id": "16",
        "alphabet": ["a", "b", "c", "d"],
        "states": ["0", "1", "2", "3", "4"],
        "initial_states": ["1"],
        "final_states": ["0"],
        "transitions": [
            "1a1",
            "1a2",
            "2b2",
            "2b3",
            "3c3",
            "3c4",
            "4d4",
            "4d0"
        ]
    },
    {
        "id": "17",
        "alphabet": ["a", "b", "c", "d"],
        "states": ["0", "1", "2", "3", "4", "5"],
        "initial_states": ["1", "2", "3", "4"],
        "final_states": ["5"],
        "transitions": [
            "1a1",
            "1a2",
            "2b2",
            "2b3",
            "3c3",
            "3c4",
            "4d4",
            "4d5",
            "5a0",
            "5b0",
            "5c0",
            "5d0"
        ]
    },
    {
        "id": "18",
        "alphabet": ["a", "b", "c", "d"],
        "states": ["0", "1", "2", "3", "4"],
        "initial_states": ["1"],
        "final_states": ["0"],
        "transitions": [
            "1a2",
            "1b3",
            "1c4",
            "1d0",
            "2a2",
            "2b3",
            "2c4",
            "2d0",
            "3b3",
            "3c4",
            "3d0",
            "4c4",
            "4d0"
        ]
    },
    {
        "id": "19",
        "alphabet": ["a"],
        "states": ["0", "1", "2"],
        "initial_states": ["1"],
        "final_states": ["0"],
        "transitions": [
            "1a2",
            "2a0",
            "0a0"
        ]
    },
    {
        "id": "20",
        "alphabet": ["a", "b", "c", "d"],
        "states": ["0", "1", "2", "3", "4", "5", "6", "7", "8"],
        "initial_states": ["1", "6", "7", "8", "0"],
        "final_states": ["5"],
        "transitions": [
            "1a2",
            "2b3",
            "3c4",
            "4d5",
            "5d0",
            "6a2",
            "7b3",
            "8c4"
        ]
    },
    {
        "id": "21",
        "alphabet": ["a", "b", "c", "d"],
        "states": ["0", "1", "2", "3"],
        "initial_states": ["1"],
        "final_states": ["1"],
        "transitions": [
            "1a2",
            "2b3",
            "3c0",
            "0d1"
        ]
    },
    {
        "id": "22",
        "alphabet": ["a", "b", "c", "d"],
        "states": ["0", "1", "2", "3"],
        "initial_states": ["1"],
        "final_states": ["1"],
        "transitions": [
            "1a0",
            "1a3",
            "1a2",
            "2b3",
            "3c0",
            "0d"
        ]
    },
    {
        "id": "23",
        "alphabet": ["a", "b", "c", "d"],
        "states": ["0", "1", "2", "3", "4"],
        "initial_states": ["1"],
        "final_states": ["0"],
        "transitions": [
            "1a2",
            "2b3",
            "3c4",
            "4d0",
            "2a2",
            "3b3",
            "4c4",
            "0d0"
        ]
    },
    {
        "id": "24",
        "states": ["0", "1", "2", "3", "4"],
        "alphabet": ["a", "b", "c", "d"],
        "initial_states": ["1"],
        "final_states": ["0"],
        "transitions": [
            "1a2",
            "2b3",
            "3c4",
            "4d0",
            "1b3",
            "1c4",
            "1d0",
            "2c4",
            "2d0",
            "3d0",
            "2a2",
            "3b3",
            "4c4",
            "0d0"
        ]
    },
    {
        "id": "25",
        "states": ["0", "1", "2", "3", "4"],
        "alphabet": ["a", "b", "c", "d"],
        "initial_states": ["1"],
        "final_states": ["0"],
        "transitions": [
            "1a2",
            "2b3",
            "3c4",
            "4d0",
            "1b3",
            "1c4",
            "1d0",
            "2c4",
            "2d0",
            "3d0",
            "1a1",
            "2b2",
            "3c3",
            "4d4"
        ]
    },
    {
        "id": "26",
        "states": ["0", "1", "2", "3"],
        "alphabet": ["a", "b"],
        "initial_states": ["1"],
        "final_states": ["3"],
        "transitions": [
            "1a2",
            "1b2",
            "2a0",
            "2b3",
            "3a3",
            "3b3"
        ]
    },
    {
        "id": "27",
        "states": ["0", "1", "2"],
        "alphabet": ["a", "b"],
        "initial_states": ["1"],
        "final_states": ["0"],
        "transitions": [
            "1a2",
            "1b2",
            "2b0",
            "0a0",
            "0b0"
        ]
    },
    {
        "id": "28",
        "states": ["0", "1", "2", "3", "4", "5"],
        "alphabet": ["a"],
        "initial_states": ["1"],
        "final_states": ["0", "3"],
        "transitions": [
            "1a2",
            "2a3",
            "3a2",
            "1a4",
            "4a5",
            "5a0",
            "0a4"
        ]
    },
    {
        "id": "29",
        "states": ["0", "1", "2", "3", "4", "5"],
        "alphabet": ["a"],
        "initial_states": ["1"],
        "final_states": ["0", "3"],
        "transitions": [
            "1a2",
            "2a3",
            "3a0",
            "1a4",
            "4a5",
            "5a0",
            "0a4",
            "3a2",
            "4a3"
        ]
    },
    {
        "id": "30",
        "states": ["0", "1", "2", "3", "4"],
        "alphabet": ["a"],
        "initial_states": ["1"],
        "final_states": ["3", "0", "4"],
        "transitions": [
            "1a2",
            "2a3",
            "0a3",
            "3a4",
            "4a0"
        ]
    },
    {
        "id": "31",
        "states": ["0", "1", "2", "3", "4", "5", "6", "7"],
        "alphabet": ["a", "b"],
        "initial_states": ["0"],
        "final_states": ["7"],
        "transitions": [
            "0$1",
            "0$4",
            "1a2",
            "1$3",
            "2b1",
            "2a3",
            "3b3",
            "3$7",
            "4b5",
            "5b6",
            "6$4",
            "6$7"
        ]
    },
    {
        "id": "32",
        "states": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                   "18", "19", "20", "21"],
        "alphabet": ["a", "b", "c"],
        "initial_states": ["0"],
        "final_states": ["21"],
        "transitions": [
            "0$1",
            "1$2",
            "2$3",
            "3b4",
            "4$3",
            "2$5",
            "5$8",
            "1$6",
            "6a7",
            "7$8",
            "8c9",
            "9$21",
            "0$10",
            "10$11",
            "11$12",
            "12a13",
            "13$12",
            "11$14",
            "10$15",
            "14$17",
            "15b16",
            "16$17",
            "17$18",
            "17$20",
            "18c19",
            "19$18",
            "19$20",
            "20$21"
        ]
    },
    {
        "id": "33",
        "states": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        "alphabet": ["a", "b", "c"],
        "initial_states": ["0"],
        "final_states": ["12"],
        "transitions": [
            "0$1",
            "1$2",
            "2a3",
            "3$5",
            "5c6",
            "6$12",
            "1$4",
            "4b4",
            "4$5",
            "0$7",
            "7$8",
            "8a8",
            "8$11",
            "7$9",
            "9b10",
            "10$11",
            "11c11",
            "11$12"
        ]
    },
    {
        "id": "34",
        "states": ["0", "1", "2", "3", "4", "5", "6"],
        "alphabet": ["a", "b"],
        "initial_states": ["0"],
        "final_states": ["6"],
        "transitions": [
            "0$1",
            "1$2",
            "1a2",
            "2b3",
            "3$2",
            "3$6",
            "0$4",
            "4b5",
            "5$4",
            "5$6"
        ]
    },
    {
        "id": "35",
        "states": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        "alphabet": ["a", "b"],
        "initial_states": ["0"],
        "final_states": ["10"],
        "transitions": [
            "0$1",
            "1a2",
            "2b3",
            "3$10",
            "0$4",
            "4$5",
            "4$8",
            "5a6",
            "6b7",
            "7$5",
            "7$8",
            "8a9",
            "9$10"
        ]
    },
    {
        "id": "36",
        "states": ["0", "1", "2"],
        "alphabet": ["a", "b"],
        "initial_states": ["0", "2"],
        "final_states": ["1", "2"],
        "transitions": [
            "0a1",
            "0b1",
            "0b2",
            "1b0",
            "1b2",
            "2a0",
            "2a1"
        ]
    },
    {
        "id": "37",
        "states": ["0", "1", "2", "3", "4"],
        "alphabet": ["a", "b"],
        "initial_states": ["0"],
        "final_states": ["0", "1", "2", "3", "4"],
        "transitions": [
            "0a1",
            "0b3",
            "1a2",
            "1b4",
            "2b0",
            "3b0",
            "3a1",
            "4a1"
        ]
    },
    {
        "id": "38",
        "states": ["0", "1", "2", "3"],
        "alphabet": ["a", "b"],
        "initial_states": ["0"],
        "final_states": ["0", "1", "2", "3"],
        "transitions": [
            "0a1",
            "0b3",
            "1a1",
            "1b2",
            "2a3",
            "2b3",
            "3a3",
            "3b3"
        ]
    },
    {
        "id": "39",
        "states": ["0", "1", "2", "3"],
        "alphabet": ["a", "b"],
        "initial_states": ["0", "1", "3"],
        "final_states": ["1"],
        "transitions": [
            "0a1",
            "0b2",
            "1a1",
            "1b2",
            "2a0",
            "2b1",
            "3a1",
            "3a2"
        ]
    },
    {
        "id": "40",
        "states": ["0", "1", "2"],
        "alphabet": ["a", "b"],
        "initial_states": ["0", "1"],
        "final_states": ["2", "0"],
        "transitions": [
            "0b1",
            "0b2",
            "1a0",
            "1a2",
            "1b2",
            "2a0"
        ]
    },
    {
        "id": "41",
        "states": ["0", "1", "2", "3", "4", "5"],
        "alphabet": ["a", "b"],
        "initial_states": ["0"],
        "final_states": ["1", "4", "3", "2"],
        "transitions": [
            "0a1",
            "1a2",
            "2a2",
            "1b3",
            "2b3",
            "3a5",
            "3b5",
            "0b4",
            "4a5",
            "4b5"
        ]
    },
    {
        "id": "42",
        "states": ["0", "1", "2", "3", "4"],
        "alphabet": ["a", "b", "c"],
        "initial_states": ["1"],
        "final_states": ["1"],
        "transitions": [
            "3a3",
            "3b3",
            "3c3",
            "0a3",
            "0c3",
            "0b1",
            "1a0",
            "1b2",
            "2b4",
            "2c4",
            "4a4",
            "4b4",
            "4c4"
        ]
    },
    {
        "id": "43",
        "states": ["0", "1", "2", "3", "4", "5", "6", "7"],
        "alphabet": ["a", ""],
        "initial_states": ["0"],
        "final_states": ["2"],
        "transitions": [
            "0a0",
            "0b0",
            "0b1",
            "2a2",
            "2b2",
            "0b1",
            "1a2"
        ]
    },
    {
        "id": "44",
        "states": ["0", "1", "2", "3"],
        "alphabet": ["a", "b"],
        "initial_states": ["0"],
        "final_states": ["3", "2"],
        "transitions": [
            "0a1",
            "0a2",
            "0b2",
            "1b3",
            "3a3",
            "3b3",
            "3a2",
            "3b2",
            "2a3",
            "2b2"
        ]
    }
]
