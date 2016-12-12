using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Chip : MonoBehaviour {

    public int value;

	// Use this for initialization
	void Start () {
        
    }
	
	// Update is called once per frame
	void Update () {
		
	}

    public void SetValue(int value) {
        this.value = value;
        IDText IdText = transform.GetComponentInChildren<IDText>();
        IdText.SetID(value);
    }
}
