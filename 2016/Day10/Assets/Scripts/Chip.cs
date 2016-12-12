using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Chip : MonoBehaviour {

    public int value;

    public void SetValue(int value) {
        this.value = value;
        IDText IdText = transform.GetComponentInChildren<IDText>();
        IdText.SetID(value);
    }
}
