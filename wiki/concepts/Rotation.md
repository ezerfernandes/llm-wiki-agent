---
title: "Rotation"
type: concept
tags: [analytic-geometry, linear-algebra, foundational, robotics, graphics]
sources: [mml-ch03-analytic-geometry, mml-book]
last_updated: 2026-06-04
---

# Rotation

A **rotation** is a linear mapping — more precisely an **automorphism** of a Euclidean vector space — that rotates a plane by an angle $\theta$ about the origin (the origin is a fixed point) ([[mml-ch03-analytic-geometry|MML Ch 3]] §3.9). By convention, a positive angle $\theta>0$ rotates **counterclockwise**. Rotations are a special class of [[OrthogonalMatrix|orthogonal transformations]] — the length- and angle-preserving linear maps of §3.4.

## Rotations in $\mathbb{R}^2$

Rotating the standard basis by $\theta$ gives the **rotation matrix** ([[mml-book]] Eq. 3.76):

$$\mathbf{R}(\theta) = \begin{bmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{bmatrix}, \qquad \Phi(\mathbf{e}_1)=\begin{bmatrix}\cos\theta\\\sin\theta\end{bmatrix},\;\Phi(\mathbf{e}_2)=\begin{bmatrix}-\sin\theta\\\cos\theta\end{bmatrix}.$$

The rotated vectors stay linearly independent, so a rotation performs a **basis change** ([[BasisChange]]).

## Rotations in $\mathbb{R}^3$

A 3-D rotation rotates a 2-D plane about a 1-D axis. The three planar rotations about the standard basis vectors ([[mml-book]] Eqs. 3.77–3.79):

$$\mathbf{R}_1(\theta)=\begin{bmatrix}1&0&0\\0&\cos\theta&-\sin\theta\\0&\sin\theta&\cos\theta\end{bmatrix},\;
\mathbf{R}_2(\theta)=\begin{bmatrix}\cos\theta&0&\sin\theta\\0&1&0\\-\sin\theta&0&\cos\theta\end{bmatrix},\;
\mathbf{R}_3(\theta)=\begin{bmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{bmatrix}.$$

"Counterclockwise" in $>2$ dimensions means looking at the axis head-on, from its tip toward the origin.

## Rotations in $n$ dimensions: Givens rotations

[[mml-book]] Definition 3.11: a **Givens rotation** $\mathbf{R}_{ij}(\theta)$ fixes $n-2$ dimensions and rotates the 2-D $(i,j)$-plane. It equals the identity $\mathbf{I}_n$ except $r_{ii}=\cos\theta$, $r_{ij}=-\sin\theta$, $r_{ji}=\sin\theta$, $r_{jj}=\cos\theta$ ($1\leq i<j\leq n$). For $n=2$ it recovers the 2-D rotation matrix.

## Properties of rotations (§3.9.4)

- **Preserve distances**: $\|\mathbf{x}-\mathbf{y}\|=\|\mathbf{R}_\theta(\mathbf{x})-\mathbf{R}_\theta(\mathbf{y})\|$.
- **Preserve angles**: the angle between $\mathbf{R}_\theta\mathbf{x}$ and $\mathbf{R}_\theta\mathbf{y}$ equals that between $\mathbf{x}$ and $\mathbf{y}$.
- **Generally non-commutative in 3+ dimensions** — order matters. Only in 2-D are rotations commutative, $\mathbf{R}(\phi)\mathbf{R}(\theta)=\mathbf{R}(\theta)\mathbf{R}(\phi)$, forming an Abelian group (under multiplication) when about the same point (e.g. the origin).

A rotation matrix is orthogonal with $\det=+1$ (a "proper" rotation); $\det=-1$ would include a reflection/flip.

## ML / applied uses

- **Robotics** — rotating joints of a robotic arm to grasp/place objects ([[mml-book]] Fig. 3.15).
- **Computer graphics** — object/camera transforms.
- **Pose estimation, point-cloud registration** (e.g. ICP), data augmentation by rotation.

## Connections

- [[mml-ch03-analytic-geometry]] — §3.9 canonical reference (Eqs. 3.74–3.81).
- [[OrthogonalMatrix]] — rotations are orthogonal matrices ($\det=+1$).
- [[BasisChange]] / [[TransformationMatrix]] — a rotation is a basis-changing linear map.
- [[Angle]] / [[Norm]] / [[Metric]] — the quantities rotations preserve.
