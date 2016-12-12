using System.Collections;
using System.Collections.Generic;
using UnityEngine;

enum BotStatus { IDLE, DELIVER_LOW, DELIVER_HIGH };

public class Bot : MonoBehaviour {

    public int botId;
    public float movementSpeed;
    public float rotateSpeed;

    private GameObject lowTarget;
    private GameObject highTarget;
    private List<GameObject> chips;
    private GameObject leftClaw;
    private GameObject rightClaw;
    private IDText botIdText;

    private BotStatus status = BotStatus.IDLE;
    private bool deliveredLow = false;
    private bool deliveredHigh = false;

	// Use this for initialization
	void Awake () {
        chips = new List<GameObject>();
        leftClaw = transform.Find("LeftClaw").gameObject;
        rightClaw = transform.Find("RightClaw").gameObject;
        // Set ID text on BotIDText
        botIdText = transform.GetComponentInChildren<IDText>();
        botIdText.SetID(botId);
	}
	
	// Update is called once per frame
	void Update () {
        // Figure out where to aim for
        GameObject currentTarget = lowTarget;
        switch(status) {
            case BotStatus.IDLE:
                return;
            case BotStatus.DELIVER_LOW:
                currentTarget = lowTarget;
                break;
            case BotStatus.DELIVER_HIGH:
                currentTarget = highTarget;
                break;
        }
        if (botId == 115) {
            Debug.Log(status);
            Debug.Log(currentTarget.GetComponent<Bot>().botId);
        }
        // Move towards target
        Vector3 toTarget = currentTarget.transform.position - transform.position;
        toTarget.Normalize();
        // Rotate towards output
        transform.rotation = Quaternion.LookRotation(Vector3.forward, currentTarget.transform.position - transform.position);
        transform.Translate(Vector3.up * movementSpeed);
    }

    public void SetID(int id) {
        this.botId = id;
        botIdText.SetID(botId);
    }

    public void SetLowTarget(GameObject target) {
        this.lowTarget = target;
    }

    public void SetHighTarget(GameObject target) {
        this.highTarget = target;
    }

    private void GiveChipTo(int chipIndex, GameObject obj) {
        GameObject chip = chips[chipIndex];
        chips.RemoveAt(chipIndex);
        Bot otherBot = obj.GetComponent<Bot>();
        if (otherBot == null) {
            OutputBin otherOutput = obj.GetComponent<OutputBin>();
            otherOutput.GiveChip(chip);
            Debug.Log("Bot " + botId.ToString() + " gives chip to output");
        } else {
            otherBot.GiveChip(chip);
            Debug.Log("Bot " + botId.ToString() + " gives chip to bot "+otherBot.botId.ToString());
        }
    }

    public void OnTriggerEnter2D(Collider2D other) {
        if (status != BotStatus.IDLE) {
            if (other.gameObject == lowTarget && !deliveredLow) {
                if (chips.Count == 1) {
                    GiveChipTo(0, lowTarget);
                    deliveredLow = true;
                    status = BotStatus.IDLE;
                }
                else if (chips.Count == 2) {
                    if (chips[0].GetComponent<Chip>().value > chips[1].GetComponent<Chip>().value) {
                        GiveChipTo(1, lowTarget);
                        deliveredLow = true;
                        status = BotStatus.DELIVER_HIGH;
                    }
                    else {
                        GiveChipTo(0, lowTarget);
                        deliveredLow = true;
                        status = BotStatus.DELIVER_HIGH;
                    }
                }
                else {
                    Debug.Log("no chips");
                    Debug.Log(chips.Count);
                    status = BotStatus.IDLE;
                }
            }
            if (other.gameObject == highTarget && !deliveredHigh) {
                if (chips.Count == 1) {
                    GiveChipTo(0, highTarget);
                    deliveredHigh = true;
                    status = BotStatus.IDLE;
                }
                else if (chips.Count == 2) {
                    if (chips[0].GetComponent<Chip>().value > chips[1].GetComponent<Chip>().value) {
                        GiveChipTo(0, highTarget);
                        deliveredHigh = true;
                        status = BotStatus.DELIVER_LOW;
                    }
                    else {
                        GiveChipTo(1, highTarget);
                        deliveredHigh = true;
                        status = BotStatus.DELIVER_LOW;
                    }
                }
                else {
                    Debug.Log("no chips");
                    Debug.Log(chips.Count);
                    status = BotStatus.IDLE;
                }
            }
        }
    }

    public void GiveChip(GameObject chip) {
        chips.Add(chip);
        if(chips.Count == 1) {
            // Reparent the chip to the left claw and position correctly
            chip.transform.parent = leftClaw.transform;
            chip.transform.localPosition = new Vector3(0f, 0.85f, 0f);
        }
        if(chips.Count == 2) {
            // Reparent the chip to the right claw asnd position correctly
            chip.transform.parent = rightClaw.transform;
            chip.transform.localPosition = new Vector3(0f, 0.85f, 0f);
            // Chip capacity reached, start delivering chips
            status = BotStatus.DELIVER_LOW;
        }
    }
}
