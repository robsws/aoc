using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;
using UnityEngine;

public class Manager : MonoBehaviour {

    public string inputFilename = @"Assets\Input\input.txt";
    public GameObject chipPrefab;
    public GameObject botPrefab;
    public GameObject outputPrefab;

    private Dictionary<int, GameObject> bots;
    private Dictionary<int, GameObject> outputs;

	// Use this for initialization
	void Start () {
        // Load in the file
        bots = new Dictionary<int, GameObject>();
        outputs = new Dictionary<int, GameObject>();
        Regex inputRegex = new Regex(@"^value (\d+) goes to bot (\d+)");
        Regex instrRegex = new Regex(@"^bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)");
        string[] lines = System.IO.File.ReadAllLines(inputFilename);
        foreach (string line in lines) {
            // Look for initial value chips to be assigned to bots
            Match inputRegexMatch = inputRegex.Match(line);
            if(inputRegexMatch.Success) {
                // Gather values from regex match
                int chipValue = Convert.ToInt32(inputRegexMatch.Groups[1].Value);
                int botId = Convert.ToInt32(inputRegexMatch.Groups[2].Value);
                // Generate a chip
                GameObject chip = (GameObject)Instantiate(chipPrefab, Vector3.zero, Quaternion.identity);
                chip.GetComponent<Chip>().SetValue(chipValue);
                // Add bot to set
                GameObject bot = AddBot(botId);
                // Give bot the chip
                bot.GetComponent<Bot>().GiveChip(chip);
            } else {
                // Look for instructions to give to bots
                Match instrRegexMatch = instrRegex.Match(line);
                if(instrRegexMatch.Success) {
                    // Gather values from regex match
                    int botId = Convert.ToInt32(instrRegexMatch.Groups[1].Value);
                    string lowOutputType = instrRegexMatch.Groups[2].Value;
                    int lowOutputId = Convert.ToInt32(instrRegexMatch.Groups[3].Value);
                    string highOutputType = instrRegexMatch.Groups[4].Value;
                    int highOutputId = Convert.ToInt32(instrRegexMatch.Groups[5].Value);
                    // Add bot to dictionary
                    GameObject bot = AddBot(botId);
                    Bot botDriver = bot.GetComponent<Bot>();
                    // Add outputs (or output bots) to respective collections
                    GameObject lowTarget;
                    GameObject highTarget;
                    if (lowOutputType.Equals("output")) {
                        lowTarget = AddOutput(lowOutputId);
                    } else {
                        lowTarget = AddBot(lowOutputId);
                    }
                    if(highOutputType.Equals("output")) {
                        highTarget = AddOutput(highOutputId);
                    } else {
                        highTarget = AddBot(highOutputId);
                    }
                    // Set up bot directions
                    botDriver.SetLowTarget(lowTarget);
                    botDriver.SetHighTarget(highTarget);
                } else {
                    // Bad line
                    Debug.Log("Bad line: " + line);
                }
            }
        }
        // Set up bot positions
        float leftOfWorldX = Camera.main.ViewportToWorldPoint(new Vector3(0, 0)).x;
        float rightOfWorldX = Camera.main.ViewportToWorldPoint(new Vector3(1, 0)).x;
        float bottomOfWorldY = Camera.main.ViewportToWorldPoint(new Vector3(0, 0)).y;
        float topOfWorldY = Camera.main.ViewportToWorldPoint(new Vector3(0, 1)).y;
        float worldWidth = rightOfWorldX - leftOfWorldX;
        Renderer botBodyRenderer = botPrefab.transform.Find("Body").gameObject.GetComponent<Renderer>();
        float botWidth = botBodyRenderer.bounds.size.x;
        float botHeight = botBodyRenderer.bounds.size.y;
        int botsPerRow = (int)(worldWidth / botWidth / 2);
        Dictionary<int, GameObject>.KeyCollection botIds = bots.Keys;
        int i = 0;
        foreach (int id in botIds) {
            GameObject bot = bots[id];
            float x = leftOfWorldX + botWidth + (botWidth * 2) * (i % botsPerRow);
            float y = bottomOfWorldY + botHeight + (botHeight * 2) * (int)(i / botsPerRow);
            bot.transform.position = new Vector3(x, y, 1);
            i++;
        }
        // Set up output positions
        Dictionary<int, GameObject>.KeyCollection outputIds = outputs.Keys;
        Renderer outputImageRenderer = outputPrefab.transform.Find("OutputImage").gameObject.GetComponent<Renderer>();
        float outputWidth = outputImageRenderer.bounds.size.x;
        float outputHeight = outputImageRenderer.bounds.size.y;
        int outputsPerRow = (int)(worldWidth / outputWidth / 2);
        i = 0;
        foreach (int id in outputIds) {
            GameObject output = outputs[id];
            float x = leftOfWorldX + outputWidth + (outputWidth * 2) * (i % botsPerRow);
            float y = topOfWorldY - (outputHeight + (outputHeight * 2) * (int)(i / outputsPerRow));
            output.transform.position = new Vector3(x, y, 1);
            i++;
        }
    }

    private GameObject AddBot(int botId) {
        if (!bots.ContainsKey(botId)) {
            GameObject newBot = (GameObject)Instantiate(botPrefab, Vector3.zero, Quaternion.identity);
            newBot.GetComponent<Bot>().SetID(botId);
            bots.Add(botId, newBot);
        }
        return bots[botId];
    }

    private GameObject AddOutput(int outputId) {
        if (!outputs.ContainsKey(outputId)) {
            GameObject newOutput = (GameObject)Instantiate(outputPrefab, Vector3.zero, Quaternion.identity);
            newOutput.transform.Find("OutputIDText").GetComponent<IDText>().SetID(outputId);
            outputs.Add(outputId, newOutput);
        }
        return outputs[outputId];
    }

    // Update is called once per frame
    void Update () {
		
	}
}
